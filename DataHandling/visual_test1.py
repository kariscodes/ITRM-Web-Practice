import matplotlib.pyplot as plt

case_id = 30

def plot_test(case_id):

    if case_id == 10:
        #given y
        plt.plot([1, 2, 3, 4])
        plt.show()

    if case_id == 20:
        #given x, y
        x = range(0, 100)
        y = [v*v for v in x]
        # plt.plot(x, y)
        plt.plot(x, y, 'ro', label='value')
        plt.xlabel('X axis')
        plt.ylabel('Y axis')
        plt.title('Practice Plot 2')
        plt.legend()
        plt.show()

    if case_id == 30:
        #draw two graph together
        #given x1, y1 -- graph1
        #given x2, y2 -- graph2
        x1 = range(-100, 100); y1 = [v*v for v in x1]
        x2 = range(-100, 100); y2 = [v+5000 for v in x2]
        # plt.plot(x, y)
        plt.plot(x1, y1, 'b', label='First')
        plt.plot(x2, y2, 'r', label='Second')
        plt.xlabel('X axis')
        plt.ylabel('Y axis')
        plt.title('Practice Plot 3')
        plt.legend()
        plt.show()

    if case_id == 31:
        #draw two graph together
        #given x1, y1 -- graph1
        #given x2, y2 -- graph2
        x1 = range(0, 100); y1 = [v*v for v in x1]
        x2 = range(0, 100); y2 = [v+5000 for v in x2]
        # plt.plot(x, y)
        line1 = plt.plot(x1, y1, 'b')
        line2 = plt.plot(x2, y2, 'r')
        plt.xlabel('X axis')
        plt.ylabel('Y axis')
        plt.title('Practice Plot 3')
        plt.figlegend((line1, line2), ('First', 'Second'))
        plt.show()

    if case_id == 40:
        #given x, y
        cnt = 0
        while cnt < 100:
            cnt += 1
            x = cnt
            y = x*x
            # plt.plot(x, y)
            plt.plot(x, y, 'ro')
            plt.xlabel('X axis')
            plt.ylabel('Y axis')
            plt.title('Practice Plot 4 -- real time drawing')
            plt.pause(0.05)
        plt.show()

plot_test(case_id)

# [plot에서 사용할 수 있는 색상과 마커]
#
# 문자	색상
# b	blue(파란색)
# g	green(녹색)
# r	red(빨간색)
# c	cyan(청록색)
# m	magenta(마젠타색)
# y	yellow(노란색)
# k	black(검은색)
# w	white(흰색)
#
# 마커	의미
# o	circle(원)
# v	triangle_down(역 삼각형)
# ^	triangle_up(삼각형)
# s	square(네모)
# +	plus(플러스)
# .	point(점)