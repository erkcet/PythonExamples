####################################################
#   Calculates the number of bytes needed to
#   store a file of a given size
###################################################

def calculate_storage(filesize):
    block_size = 4096
    full_blocks = filesize//block_size
    partial_block_remainder = filesize%block_size
    if partial_block_remainder > 0:
        return (full_blocks + 1)*block_size
    return block_size*full_blocks

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192
