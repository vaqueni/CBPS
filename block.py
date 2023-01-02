import datetime
import hashlib as hasher
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





