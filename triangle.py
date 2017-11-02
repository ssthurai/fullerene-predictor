import numpy
import numpy.linalg

##########################################################################


def compute_angle(p1, p2, p3):
    d12 = numpy.linalg.norm(numpy.array(p1) - numpy.array(p2))
    d13 = numpy.linalg.norm(numpy.array(p1) - numpy.array(p3))
    d23 = numpy.linalg.norm(numpy.array(p2) - numpy.array(p3))

    return_value = numpy.arccos((d12**2 + d13**2 - d23**2) / (2 * d12 * d13))

    return return_value

##########################################################################


def compute_area(P1, p2, p3):
    d12 = numpy.linalg.norm(numpy.array(p1) - numpy.array(p2))
    d13 = numpy.linalg.norm(numpy.array(p1) - numpy.array(p3))
    d23 = numpy.linalg.norm(numpy.array(p2) - numpy.array(p3))

    s = 0.5 * (d12 + d13 + d23)
    return (s * (s - d12) * (s - d13) * (s - d23)) ** 0.5
