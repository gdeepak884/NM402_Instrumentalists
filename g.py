import zlib
import os

original_data = open('logo.png', 'rb').read()
compressed_data = zlib.compress(original_data, zlib.Z_BEST_COMPRESSION)
#o_file_size = os.path.getsize("logo.png")
compress_ratio = (float(len(original_data)) - float(len(compressed_data))) / float(len(original_data))
#print(o_file_size,"Bytes")
print('Compressed: %d%%' % (100.0 * compress_ratio))
print('Compressed: %d%%', original_data)
print('Compressed:',compressed_data)
