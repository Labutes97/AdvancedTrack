from how_to_think.chapter_11.section_1_12.Point import Point
from how_to_think.chapter_11.section_2_6.Rectangle import Rectangle
from how_to_think.test.test import test_equal

r = Rectangle(Point(0,0), 10, 5)
test_equal(r.width, 10)
test_equal(r.height, 5)

r.flip()
test_equal(r.width, 5)
test_equal(r.height, 10)
