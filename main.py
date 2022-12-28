import datetime
import hashlib as hasher
import numpy
import random

# 난이도
bits = 1


# 블록 클래스
class Block:
    def __init__(self, index, name, time, bits, data, previous_hash):
        self.index = index
        self.name = name
        self.time = time
        self.bits = bits
        self.data = data
        self.previous_hash = previous_hash
        self.hash = ""
        self.nonce = 0

    def get_block_hash(self):
        sha = hasher.sha256()
        sha.update((str(self.index) + self.name + str(self.time) + str(self.bits) + str(self.data) + str(
            self.previous_hash) + str(
            self.nonce)).encode("utf-8"))
        return sha.hexdigest()

    def mine(self):
        nonce = 0
        while not self.valid_nonce(nonce):
            nonce += 1
        print("새 블록 생성 됨: {}".format(self.hash))

    def valid_nonce(self, nonce):
        self.nonce = nonce
        self.hash = self.get_block_hash()
        i = 1
        for c in self.hash:
            if (c is not "0"):
                return False

            if (i is self.bits):
                return True
            i += 1


# Genesis 블록 생성 함수 (첫 블록)
def create_genesis_block():
    # 첫 블록은 별다른 데이터를 가지지 않는다.
    return Block(0, '', datetime.datetime.now(), bits, "Genesis Block", "0")


# 새 블록 생성
def next_block(prev_block, name, data):
    index = prev_block.index + 1
    name = name
    time = datetime.datetime.now()
    previous_hash = prev_block.hash
    block = Block(index, name, time, bits, data, previous_hash)
    block.mine()
    return block


# 블록을 저장할 체인
block_chain = [create_genesis_block()]
my_block_chain = [create_genesis_block()]

# ==================================================================================================================== #
# 게임 실행 전 세팅


for i in range(0, 1601):
    k = random.uniform(0, 100)  # 박스
    n = random.uniform(0, 1601)  # 사람
    user_name = ''
    result = ''
    if 0 < n < 10:  # 승환
        user_name = '승환'
    elif 10 <= n < 110:  # 성산
        user_name = '성산'
    elif 110 <= n < 610:  # 주호
        user_name = '주호'
    else:  # 송아
        user_name = '송아'

    if k < 80:  # 80퍼센트 확률로 꽝이다.
        result = '꽝'
    elif 80 <= k < 95:  # 15 퍼센트 확률
        result = "쿠폰"
    else:  # 5퍼센트 확률
        result = "자동차"
    block_chain.append(next_block(block_chain[len(block_chain) - 1], user_name, result))

'''

def box_loop(n, player_name):
    k = random.uniform(0, 100)

    for i in range(0, n):
        if k < 80:  # 80퍼센트 확률로 꽝이다.
            result = '꽝'

        elif 80 <= k < 95:  # 15 퍼센트 확률
            result = "쿠폰"

        elif 95 <= k <= 100:  # 5퍼센트 확률
            result = "자동차"

        block_chain.append(next_block(block_chain[len(block_chain) - 1], player_name, result))


player1 = '성산'
player2 = '승환'
player3 = '주호'
player4 = '송아'

box_loop(50, '성산')
box_loop(100, '승환')
box_loop(500, '주호')
box_loop(1000, '송아')


#전체 통계
car_count = 0
coupon_count = 0
fail_count = 0

for block in block_chain:
    if block.data == "자동차":
        car_count += 1
    elif block.data == "쿠폰":
        coupon_count += 1
    else:
        fail_count+=1

pCar = car_count/len(block_chain)
pCoupon = coupon_count/len(block_chain)
pFail = fail_count/len(block_chain)

#개인배열 생성
n1 =[] #승환
n2 =[] #성산
n3 =[] #주호
n4 =[] #송아

#개인 시행횟수
name1 = 0
name2 = 0
name3 = 0
name4 = 0

#블록에 이름으로 분배
for block in block_chain:
    if block.name == '승환':
        name1 += 1
        n1.append(block)
    elif block.name == '성산':
        name2 += 1
        n2.append(block)
    elif block.name == '주호':
        name3 += 1
        n3.append(block)
    else:
        name4 += 1
        n4.append(block)
print('승환',name1,'성산',name2,'주호',name3,'송아',name4)
'''

''' CarPrb = Label(sWin, text='자동차:' + "{:.2f}".format(pCar * 100) + '%',font=('SD산돌고딕', 30))'''

# ==================================================================================================================== #
# ==================================================================================================================== #
# ==================================================================================================================== #
# ==================================================================================================================== #
# ==================================================================================================================== #
# ==================================================================================================================== #
# ==================================================================================================================== #
# ==================================================================================================================== #

# UI만들기
from tkinter import *
from tkinter.ttk import Combobox, Treeview

win = Tk()
win.option_add("*Font", "Arial 20")
win.geometry("500x500")

r_img = [PhotoImage(file="box.png").subsample(4), PhotoImage(file="boom.png").subsample(4),
         PhotoImage(file="coupon.png").subsample(4), PhotoImage(file="car.png").subsample(3),
         PhotoImage(file="pGraph.png").subsample(2)]
# 버튼 명령 함수
global money
money = 10000000  # 천만원

global my_name
my_name = '플레이어'


def flex():
    global money
    money -= 100
    return money


'''
global count
count = 0

def count():
    global count
    count += 1
    return count
'''
global xx
xx = 200
box_x = 100
box_y = 30


def buy_window():
    boxWin = Toplevel(win)
    boxWin.geometry("500x500")
    money_label = Label(boxWin, text='gold:')
    money_label_ = Label(boxWin, text=money)

    # 박스 결과를 띄우는 창 만들기
    r_label = Label(boxWin, image=r_img[0])
    r_label.place(x=box_x, y=box_y)
    r_description = Label(boxWin, text='')
    r_description.place(x=440, y=50)

    def make_bc():
        k = random.uniform(0, 100)
        result = ''
        money_label_.config(text=flex())

        if k < 80:  # 80퍼센트 확률로 꽝이다.
            result = "꽝"
            r_label.config(image=r_img[1])
            r_label.place(x=box_x, y=box_y + 50)
        elif 80 <= k < 95:  # 15 퍼센트 확률
            result = "쿠폰"
            r_label.config(image=r_img[2])
            r_label.place(x=box_x, y=box_y)
        else:  # 5퍼센트 확률
            result = "자동차"
            r_label.config(image=r_img[3])
            r_label.place(x=box_x - 60, y=box_y + 100)

        r_description.config(text=result)
        block_chain.append(next_block(block_chain[len(block_chain) - 1], my_name, result))
        my_block_chain.append(next_block(my_block_chain[len(my_block_chain) - 1], my_name, result))

        open_box.config(text='한번 더 열기')

    # 블록체인 만드는 버튼 배치
    xx = 200
    yy = 430
    open_box = Button(boxWin, height=2, width=10)
    open_box.config(text="오픈!")
    open_box.place(x=xx, y=yy)  # 절대좌표

    money_label.place(x=340, y=1)
    money_label_.place(x=390, y=1)

    open_box.config(command=make_bc)


# 가진돈을 띄우는 창
m_text = 'money: '

# 처음 시작 페이지
title_label = Label(win, text='C.B.P.S', font=('SD산돌고딕', 100))
title_label.config(width=5, height=2)
title_label.place(x=100, y=1)

sub_title_label = Label(win, text='게임확률 검증시스템', font=('SD산돌고딕', 20))
sub_title_label.config(width=20, height=1)
sub_title_label.place(x=190, y=180)


# 구매창으로 이동하는 버튼 만들기
def search_window():
    sWin = Toplevel(win)
    sWin.geometry("500x500")

    def my_prb():  ##나의 구매조회
        my_win = Toplevel(sWin)
        my_win.geometry("500x500")

        tree_name = Label(my_win, text='구매 내역')
        tree_name.pack()

        treeview = Treeview(my_win, columns=['one', 'two', 'three'], displaycolumns=['one', 'two', 'three'])
        treeview.pack()

        treeview.column("#0", width=100, )
        treeview.heading("#0", text="시간")

        treeview.column("#1", width=350, anchor="center")
        treeview.heading("one", text="해시", anchor="center")

        treeview.column("#2", width=50, anchor="center")
        treeview.heading("two", text="결과", anchor="center")
        # [5:5+11]
        treelist = []
        for block in my_block_chain:
            treelist.append([block.hash, block.data])

        for i in range(len(treelist)):
            T = str(my_block_chain[i + 1].time)
            T = T[5:16]
            treeview.insert('', 'end', text=T, values=treelist[i + 1], iid=str(i) + "번")
        # treeview.column("#3", width=70, anchor="center")

        # treeview.heading("three", text="rank", anchor="center")

    search_button = Button(sWin, height=2, width=10)
    search_button.config(text='나의 구매조회', command=my_prb)
    search_button.place(x=xx, y=150)

    def prb():
        prb_button.place_forget()
        search_button.place_forget()

        def show_graph():
            g_win = Toplevel(sWin)
            g_win.geometry("570x410")
            graph_label = Label(g_win, image=r_img[4])
            graph_label.place(x=-10, y=0)

        graph_btn = Button(sWin, height=2, width=10, text='그래프 보기', command=show_graph)
        graph_btn.place(x=100, y=400)

        # 친구의 확률을 구하는 법 player로 검색, box_result로 어떤 거인지 물어본다.
        # player: 플레이어, 승환 성산 주호 송아
        # box_result: 자동차,쿠폰,꽝

        def find_p_set(player):
            set_count = 0
            for j in block_chain:
                if j.name == player:
                    set_count += 1
            return set_count

        def find_count(player, box_result):
            result_count = 0
            for j in block_chain:
                if j.data == box_result and j.name == player:
                    result_count += 1
            return result_count

        def find_p(player, box_result):
            if find_count(player, box_result) == 0:
                print("division zero")
                return 0
            else:
                return find_count(player, box_result) / find_p_set(player)

        def show_friend():
            f_win = Toplevel(sWin)
            f_win.geometry("500x500")
            friend_combo = Combobox(f_win)
            friend_combo['values'] = ('승환', '성산', '주호', '송아')
            friend_combo.config(state="readonly")  # 콤보 박스에 사용자가 직접 입력 불가
            friend_combo.set("선택")
            friend_combo.place(x=0, y=0)

            def show_prb():
                player = friend_combo.get()

                fBoxCountText = Label(f_win, text=player + '의 박스 오픈: ' + str(find_p_set(player)), width=15, height=2,
                                      font=('SD산돌고딕', 15))
                fBoxCountText.place(x=300, y=50)

                fCarPrb = Label(f_win, text=player + '의 자동차:' + "{:.2f}".format(find_p(player, '자동차') * 100) + '%',
                                font=('SD산돌고딕', 30))
                fCarPrb.place(x=20, y=150)
                fCarCount = Label(f_win, text=str(find_count(player, '자동차')) + '개 오픈됨', font=('SD산돌고딕', 25))
                fCarCount.place(x=330, y=150)

                fCouponPrb = Label(f_win, text=player + '의 쿠폰: ' + "{:.2f}".format(find_p(player, '쿠폰') * 100) + '%',
                                   font=('SD산돌고딕', 30))
                fCouponPrb.place(x=20, y=250)
                fCouponCount = Label(f_win, text=str(find_count(player, '쿠폰')) + '개 오픈됨', font=('SD산돌고딕', 25))
                fCouponCount.place(x=330, y=250)

                fFailPrb = Label(f_win, text=player + '의 꽝:  ' + "{:.2f}".format(find_p(player, '꽝') * 100) + '%',
                                 font=('SD산돌고딕', 30))
                fFailPrb.place(x=20, y=350)
                fFailCount = Label(f_win, text=str(find_count(player, '꽝')) + '개 오픈됨', font=('SD산돌고딕', 25))
                fFailCount.place(x=330, y=350)

            sel_btn = Button(f_win)
            sel_btn.config(command=show_prb, width=5, height=1, text='검색')
            sel_btn.place(x=265, y=4)

        friend_btn = Button(sWin, height=2, width=10, text='친구의 확률', command=show_friend)
        friend_btn.place(x=250, y=400)
        # 확률 계산
        car_count = 0
        coupon_count = 0
        fail_count = 0

        my_car_count = 0
        my_coupon_count = 0
        my_fail_count = 0
        my_count = 0
        for block in block_chain:
            if block.data == "자동차":
                car_count += 1
                if block.name == my_name:
                    my_car_count += 1
                    my_count += 1
            elif block.data == "쿠폰":
                coupon_count += 1
                if block.name == my_name:
                    my_coupon_count += 1
                    my_count += 1
            elif block.data == "꽝":
                fail_count += 1
                if block.name == my_name:
                    my_fail_count += 1
                    my_count += 1

        pCar = car_count / len(block_chain)
        pCoupon = coupon_count / len(block_chain)
        pFail = fail_count / len(block_chain)

        BoxCountText = Label(sWin, text='전체 박스 오픈: ' + str(len(block_chain) - 1), width=15, height=2,
                             font=('SD산돌고딕', 20))
        BoxCountText.place(x=300, y=0)

        myBoxCountText = Label(sWin, text='나의 박스 오픈: ' + str(my_count), width=15, height=2, font=('SD산돌고딕', 15))
        myBoxCountText.place(x=300, y=50)

        CarPrb = Label(sWin, text='자동차:' + "{:.2f}".format(pCar * 100) + '%', font=('SD산돌고딕', 30))
        CarPrb.place(x=20, y=100)
        CarCount = Label(sWin, text=str(car_count) + '개 오픈됨', font=('SD산돌고딕', 25))
        CarCount.place(x=330, y=100)

        CouponPrb = Label(sWin, text='쿠폰: ' + "{:.2f}".format(pCoupon * 100) + '%', font=('SD산돌고딕', 30))
        CouponPrb.place(x=20, y=200)
        CouponCount = Label(sWin, text=str(coupon_count) + '개 오픈됨', font=('SD산돌고딕', 25))
        CouponCount.place(x=330, y=200)

        FailPrb = Label(sWin, text='꽝:  ' + "{:.2f}".format(pFail * 100) + '%', font=('SD산돌고딕', 30))
        FailPrb.place(x=20, y=300)
        FailCount = Label(sWin, text=str(fail_count) + '개 오픈됨', font=('SD산돌고딕', 25))
        FailCount.place(x=330, y=300)

        mypCar = my_car_count / my_count
        mypCoupon = my_coupon_count / my_count
        mypFail = my_fail_count / my_count

        myCarPrb = Label(sWin, text='나의 자동차:' + "{:.2f}".format(mypCar * 100) + '%', font=('SD산돌고딕', 20))
        myCarPrb.place(x=20, y=150)
        myCarCount = Label(sWin, text=str(my_car_count) + '개 오픈됨', font=('SD산돌고딕', 15))
        myCarCount.place(x=330, y=150)

        myCouponPrb = Label(sWin, text='나의 쿠폰: ' + "{:.2f}".format(mypCoupon * 100) + '%', font=('SD산돌고딕', 20))
        myCouponPrb.place(x=20, y=250)
        myCouponCount = Label(sWin, text=str(my_coupon_count) + '개 오픈됨', font=('SD산돌고딕', 15))
        myCouponCount.place(x=330, y=250)

        myFailPrb = Label(sWin, text='나의 꽝:  ' + "{:.2f}".format(mypFail * 100) + '%', font=('SD산돌고딕', 20))
        myFailPrb.place(x=20, y=350)
        myFailCount = Label(sWin, text=str(my_fail_count) + '개 오픈됨', font=('SD산돌고딕', 15))
        myFailCount.place(x=330, y=350)

    prb_button = Button(sWin, height=2, width=10)
    prb_button.config(text='확률조회', command=prb)
    prb_button.place(x=xx, y=250)


buy_page_button = Button(win, height=2, width=10)
buy_page_button.config(text="랜덤박스\n구매하기")
buy_page_button.place(x=80, y=300)  # 절대좌표
buy_page_button.config(command=buy_window)

# 구매조회창으로 이동하는 버튼 만들기
search_page_button = Button(win, height=2, width=10)
search_page_button.config(text="구매조회")
search_page_button.place(x=280, y=300)  # 절대좌표
search_page_button.config(command=search_window)

# 돈
m_label = Label(win, text=m_text + str(money))
m_label.config(width=15, height=1)
# m_label.place(x=350, y=400)
m_label.place_forget()

# 박스 연 시간을 띄우는 창
t_text = 'time: '
t_label = Label(win, text=t_text)
t_label.config(width=15, height=1)
# t_label.place(x=200, y=120)
t_label.place_forget()

# btn.place(relx = 0.4 , rely = 0.9)#상대좌표

# 블록체인 만들도록 명령하기


win.mainloop()

# ==================================================================================================================== #


# 블록 생성 + 작업증명(POW)
# block_chain.append(next_block(block_chain[len(block_chain) - 1], "안녕하세요"))
# block_chain.append(next_block(block_chain[len(block_chain) - 1], "테스트"))
# block_chain.append(next_block(block_chain[len(block_chain) - 1], "삘릴릴릴리 !!!"))

# 블록체인의 블록 정보 출력
# for block in block_chain:
#     print("블록해시: {}\n시간: {}\nNonce: {}\n블록 데이터: {}\n\n".format(block.hash, block.time, block.nonce, block.data))
