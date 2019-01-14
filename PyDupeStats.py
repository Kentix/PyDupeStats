# --Usage-- PyDupeStats.py "D:\Path\To\Inspect" ChunkInspectionSizeInByte
# --Usage Example-- PyDupeStats.py "E:\Data\Virtual_Machines" 16384

import os
import sys
import hashlib
from datetime import datetime

# TODO: Add argument for scanning only a maximum of x GB of bytes,
# potentially random chunk layouts

# TODO: Add keyword arguments for ease of use and clarity

# TODO: Add default value for chunk size, i.e. 16384

folder_path = sys.argv[1]

# Chunk size is obtained from argument 2 of 2
chunk_size = sys.argv[2]


# TODO: Generate temporary file without the need to solicit from the user
# TODO: Intermediate until auto temp file generation, default to current path
# of python file
hashes_file_path = input("Enter exact path + file for temp hash storage: ")

sha1_hash = hashlib.sha1()
object_counter = 0
chunk_agg = 0
datapath_issues = 0
start_time = datetime.now()
chunk_thresh_not_met = 0
objects_bytes_sum = 0

# TODO: Get recursive file count and size summation prior to a complete
# run (potentially use for progress)

for root, dirs, files in os.walk(folder_path, topdown=False):
    for name in files:
        chunk_iterator = 0
        raw_chunk_count = 0
        # Read each 'x' (size in bytes) chunk of each file in specified path
        # until end of file
        try:
            object_size = os.path.getsize(os.path.join(root, name))
            if int(object_size) >= int(chunk_size):
                objects_bytes_sum += object_size
                raw_chunk_count = object_size / int(chunk_size, 10)
                with open((os.path.join(root, name)), 'rb') as current_file:
                    while True:
                        buff_chunk = current_file.read(int(chunk_size))
                        if not buff_chunk:
                            break
                        sha1_hash = hashlib.sha1()
                        chunk_iterator += 1
                        # For each 'x' chunk, run sha1_hash hash on the chunk
                        sha1_hash.update(buff_chunk)
                        # Albeit inefficient, it was quick and dirty;
                        # Write the computed sha1_hash
                        # hash to file/db
                        hash_row_data = str(sha1_hash.hexdigest()) + '\n'
                        with open(hashes_file_path, 'a') as csv_file_object:
                            csv_file_object.write(hash_row_data)
                        csv_file_object.close()
            else:
                chunk_thresh_not_met += 1
        except:
            datapath_issues += 1
            raise NameError('FAIL-DP001')

        object_counter += 1
        chunk_agg += raw_chunk_count

# TODO: Dilineate between end_time of file byte stream hashing and
# recording vs. hash file duplicate line analysis
end_time = datetime.now()
elapsed_time = end_time - start_time
elapsed_time_tuple = divmod(
    elapsed_time.days * 86400 + elapsed_time.seconds, 60
    )
object_bytes_agg_mb = objects_bytes_sum / 1024 / 1024
object_bytes_agg_gb = objects_bytes_sum / 1024 / 1024 / 1024

if elapsed_time_tuple[1] >= 1:
        average_megabytes_second = object_bytes_agg_mb / (
            (elapsed_time.days * 86400) + elapsed_time.seconds
            )
        average_gigabytes_minute = (
            object_bytes_agg_mb / (
                (elapsed_time.days * 86400) + elapsed_time.seconds
                )
            ) * 60 / 1024
        average_gigabytes_hour = (
            object_bytes_agg_mb / (
                (elapsed_time.days * 86400) + elapsed_time.seconds
                )
            ) * 60 / 1024 * 60
else:
    average_megabytes_second = object_bytes_agg_mb

duplicate_counter = 0

with open(hashes_file_path) as f:
    seen = set()
    for line in f:
        # line_lower = line.lower()
        if line in seen:
            duplicate_counter += 1
        else:
            seen.add(line)

# TODO: Write printed results to file or similar, perhaps
# to the temporary hash file
print("--------RUN COMPLETED---------")
print("Start Time:", str(start_time))
print("End Time:", str(end_time))
print(
    "Elapsed Time:", str(
        elapsed_time_tuple[0]
        ), "Minutes and", str(elapsed_time_tuple[1]), "Seconds"
    )
print("Average Speed in MBytes/Second:", round(average_megabytes_second, 2))
print("Average Speed in GBytes/Minute:", round(average_gigabytes_minute, 2))
print("Average Speed in GBytes/Hour:", round(average_gigabytes_hour, 2))
print(
    "# of chunks with the same", chunk_size,
    "byte chunk hash:", duplicate_counter
    )
print("Chunk Size in Bytes:", chunk_size)
print("File Path for Recording Hashes:", hashes_file_path)
print("Total objects processed:", object_counter)
print("Total Bytes processed:", "{:,}".format(objects_bytes_sum))
print("Total MBytes processed:", "{:,}".format(
    int(object_bytes_agg_mb)
    ), "Megabytes (Approx.)")
print("Total GBytes processed:", round(
    object_bytes_agg_gb, 2
    ), "Gigabytes (Approx.)")
print("Minimum Gigabytes of duplicate data:", round(
    int(chunk_size, 10) * duplicate_counter / 1024 / 1024 / 1024 / 2, 2
), "Gigabytes (Approx.)")
print("Total Chunks in Scope:", int(chunk_agg))
print("Total objects not meeting chunk threshold:", chunk_thresh_not_met)