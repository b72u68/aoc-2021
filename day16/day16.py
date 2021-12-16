import os
import sys


HEX_TO_BINARY = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100',
                 '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001',
                 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110',
                 'F': '1111'}


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    f = open(file_dir)

    data = "".join([HEX_TO_BINARY[hex] for hex in f.readlines()[0].strip("\n")])

    return data


class Packet:
    def __init__(self, version, type):
        self.version = version
        self.type = type

    def version_sum(self):
        return self.version

    def evaluate(self):
        return 0


class ValuePacket(Packet):
    def __init__(self, version, type, value):
        super().__init__(version, type)
        self.value = value

    def evaluate(self):
        return int(self.value, 2)


class OperatorPacket(Packet):
    def __init__(self, version, type, subpackets):
        super().__init__(version, type)
        self.subpackets = subpackets

    def version_sum(self):
        return sum([p.version_sum() for p in self.subpackets]) + self.version

    def evaluate(self):
        if self.type == 0:
            return sum(self.evaluate_subpackets())
        elif self.type == 1:
            result = 1
            for value in self.evaluate_subpackets():
                result *= value
            return result
        elif self.type == 2:
            return min(self.evaluate_subpackets())
        elif self.type == 3:
            return max(self.evaluate_subpackets())
        elif self.type == 5:
            return int(self.subpackets[0].evaluate() > self.subpackets[1].evaluate())
        elif self.type == 6:
            return int(self.subpackets[0].evaluate() < self.subpackets[1].evaluate())
        elif self.type == 7:
            return int(self.subpackets[0].evaluate() == self.subpackets[1].evaluate())

    def evaluate_subpackets(self):
        return [p.evaluate() for p in self.subpackets]


def parse_packet(binary, i=0):
    while i < len(binary):
        V = int(data[i:i+3], 2)
        i += 3
        T = int(data[i:i+3], 2)
        i += 3
        if T == 4:
            value = ""
            while True:
                signal_bit = binary[i]
                i += 1
                value += binary[i:i+4]
                i += 4
                if signal_bit == "0":
                    break
            return ValuePacket(V, T, value), i
        else:
            L = binary[i]
            i += 1
            subpackets = []
            if L == "0":
                length_int_bits = int(binary[i:i+15], 2)
                i += 15
                stop = length_int_bits + i
                while i < stop:
                    subpacket, i = parse_packet(binary, i)
                    subpackets.append(subpacket)
            elif L == "1":
                L = int(binary[i:i+11], 2)
                i += 11
                for j in range(L):
                    subpacket, i = parse_packet(binary, i)
                    subpackets.append(subpacket)
            return OperatorPacket(V, T, subpackets), i


# solution for part 1
def part1(data):
    packets = parse_packet(data)[0]
    return packets.version_sum()


# solution for part 2
def part2(data):
    packets = parse_packet(data)[0]
    return packets.evaluate()


if __name__ == "__main__":

    filename = "data.txt"

    if len(sys.argv) >= 2:
        filename = sys.argv[1]

    try:
        data = get_data(filename)
        print(part1(data))
        print(part2(data))

    except Exception as e:
        print(e)
