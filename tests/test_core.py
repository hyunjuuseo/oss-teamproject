import pytest
from PIL import Image, ImageDraw

from legibly.core import detect_text_regions


def save_note(tmp_path, rectangles=(), size=(200, 100), mode="L", fill="black"):
    """Draw filled rectangles on a white page and return the saved path."""
    img = Image.new(mode, size, "white")
    draw = ImageDraw.Draw(img)
    for rect in rectangles:
        draw.rectangle(rect, fill=fill)
    path = tmp_path / "note.png"
    img.save(path)
    return str(path)


def bboxes(regions):
    return [region["bbox"] for region in regions]


def test_two_lines_are_found_top_to_bottom(tmp_path):
    path = save_note(tmp_path, [(20, 50, 149, 64), (10, 10, 99, 24)])
    assert bboxes(detect_text_regions(path)) == [[10, 10, 100, 25], [20, 50, 150, 65]]


def test_region_image_matches_bbox(tmp_path):
    path = save_note(tmp_path, [(30, 40, 79, 49)])
    (region,) = detect_text_regions(path)
    assert region["image"].size == (50, 10)


def test_blank_page_returns_empty_list(tmp_path):
    assert detect_text_regions(save_note(tmp_path)) == []


def test_line_touching_bottom_edge_is_kept(tmp_path):
    path = save_note(tmp_path, [(0, 90, 199, 99)])
    assert bboxes(detect_text_regions(path)) == [[0, 90, 200, 100]]


def test_specks_shorter_than_min_height_are_dropped(tmp_path):
    path = save_note(tmp_path, [(5, 5, 7, 7), (10, 30, 99, 44)])  # 3 px speck
    assert bboxes(detect_text_regions(path)) == [[10, 30, 100, 45]]
    assert len(detect_text_regions(path, min_height=1)) == 2


def test_rgb_image_is_accepted_and_file_not_changed(tmp_path):
    path = save_note(tmp_path, [(10, 10, 59, 19)], mode="RGB", fill=(0, 0, 255))
    before = open(path, "rb").read()
    assert bboxes(detect_text_regions(path)) == [[10, 10, 60, 20]]
    assert open(path, "rb").read() == before


def test_light_gray_ink_follows_threshold(tmp_path):
    path = save_note(tmp_path, [(10, 10, 59, 19)], fill=180)
    assert detect_text_regions(path) == []
    assert bboxes(detect_text_regions(path, threshold=200)) == [[10, 10, 60, 20]]


def test_missing_file_raises_file_not_found(tmp_path):
    with pytest.raises(FileNotFoundError):
        detect_text_regions(str(tmp_path / "nope.png"))


def test_non_image_file_raises_value_error(tmp_path):
    path = tmp_path / "note.txt"
    path.write_text("not an image")
    with pytest.raises(ValueError):
        detect_text_regions(str(path))


@pytest.mark.parametrize("kwargs", [{"threshold": 256}, {"threshold": -1}, {"min_height": 0}])
def test_bad_arguments_raise_value_error(tmp_path, kwargs):
    with pytest.raises(ValueError):
        detect_text_regions(save_note(tmp_path), **kwargs)
