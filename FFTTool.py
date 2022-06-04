import numpy as np
import sys

class ZeroPadding:
    def __init__(self, data, position="both", add_zeroarray="left"):
        self.position = position
        self.data = data
        self.nframe = len(data)
        self.add_zeroarray = add_zeroarray
 

    def process(self):
        """
        Flow process of zeropadding.
        """
        zeropadding_nframe = self.next_power2(self.nframe) - self.nframe
        if self.position == "both":
            return self.both_zeropadding(zeropadding_nframe)
        elif self.position == "left":
            return self.left_zeropadding(zeropadding_nframe)
        elif self.position == "right":
            return self.right_zeropadding(zeropadding_nframe)
        else:
            print("Argument error. Argument candidates are both, left, right.")
            sys.exit()


    def next_power2(self, N):
        """
        Include N to next power of 2.
        For example, include 2**(n+1) from 2**n.
        """
        power2 = 0
        while N > 2**power2:
            power2 = power2 + 1
        return 2**power2


    def both_zeropadding(self, zeropadding_nframe):
        """
        Add 0 data left and right side each other how to zeropadding.
        """
        left_zeropadding_nframe = None
        right_zeropadding_nframe = None
        half_zeropadding_nframe = None
        print("nframe : {0}".format(zeropadding_nframe))
        if zeropadding_nframe % 2 != 0:
            if self.add_zeroarray == "left":
                left_zeropadding_nframe = int(zeropadding_nframe / 2) + 1
                right_zeropadding_nframe = int(zeropadding_nframe / 2)
                print("Throught left")
            elif self.add_zeroarray == "right":
                left_zeropadding_nframe = int(zeropadding_nframe / 2)
                right_zeropadding_nframe = int(zeropadding_nframe / 2) + 1
                print("Throught right")
            else:
                print("Argument error. Argument candidates are left or right.")
                sys.exit()
                
            left_zero_array = np.zeros(left_zeropadding_nframe)
            right_zero_array = np.zeros(right_zeropadding_nframe)
            x = np.append(left_zero_array, self.data)
            x = np.append(x, right_zero_array)
            return x
        else:
            half_zeropadding_nframe = int(zeropadding_nframe / 2)
            left_zero_array = np.zeros(half_zeropadding_nframe)
            right_zero_array = np.zeros(half_zeropadding_nframe)
            x = np.append(left_zero_array, self.data)
            x = np.append(x, right_zero_array)
            return x


    def left_zeropadding(self, zeropadding_nframe):
        """
        Add 0 data left side how to zeropadding.
        """
        left_array = np.zeros(zeropadding_nframe)
        x = np.append(left_array, self.data)
        return x


    def right_zeropadding(self, zeropadding_nframe):
        """
        Add 0 data right side how to zeropadding.
        """
        right_array = np.zeros(zeropadding_nframe)
        x = np.append(self.data, right_array)
        return x