import struct
import os
if __name__=='__main__':
    # filepath='/home/kyaking/downloads/pic/rose_seq_auto/matches/DSC_3428.desc'
    filepath = '/home/kyaking/downloads/pic/rose_seq_auto/matches/matches.f.bin'
    binfile = open(filepath,'rb')
    size = os.path.getsize(filepath)
    for i in range(size):
        data = binfile.read(1)
        num = struct.unpack('B',data)[0]
        print(num)
        # print(data)
    binfile.close()

#
# def xshow(filename, nx, nz):
#     f = open(filename, "rb")
#     pic = np.zeros((nx, nz))
#     for i in range(nx):
#         for j in range(nz):
#             data = f.read(4)
#             elem = struct.unpack("f", data)[0]
#             pic[i][j] = elem
#     f.close()
#     return pic
#
# plt.imsave('output.tiff', img, format='tiff', cmap=plt.cm.gray)