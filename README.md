# PyDupeStats
**A Python tool used to detect duplicate blocks of data in a given data set**

PyDupeStats is a tool written in Python for analyzing file sets for duplicate blocks/chunks. This is useful for determining inter-file and intra-file similarity at varying chunk sizes.
I have used this in situations where a vendor, platform, or technology is claiming storage reduction relating to deduplication of any object that can be addressed at the file or applicable protocol access layer. This tool can also be used to determine the feasibility of applying deduplication techniques to a given dataset.


## Getting started

This was developed and tested in Python 3.x on Windows 10. There is no installation necessary aside from having Python 3.x installed.

### To get started:

1. Clone the repo or simply download the PyDupeStats.py file
2. From a command prompt or shell, run 'python PyDupeStats.py "\\\\Server\Path\To\Analyze" desired_chunk_size'
    * e.g. python PyDupeStats.py "\\\\us-namespace\finance\payroll" 16384
    * In the example above, PyDupeStats will run, recursively scan every file in the given UNC path and inspect each file at a chunk size of 16384 bytes.
    * Note: If running on Windows, this assumes that python binaries are included in PATH system variables on Windows
3. Enter the location and name of the temporary file which will record the hashes for the given run.
    * e.g. S:\Temp\HashRun_VirtualMachines_16384Chunk.hash
4. After all the files are scanned, printed output will be displayed.
5. Runtime duration is dependent on many things including hardware abilities, file count, and the chunk size specified, among others.

**---Example Input/Output---**

    python "S:\PythonProjects\PyDupeStats\PyDupeStats.py" "E:\Binaries\ISO_Files" 8192
    Enter exact path + file for temp hash storage S:\Temp\ISO_Files_E_Drive_8192.pyd
    --------RUN COMPLETED---------
    Start Time: 2019-01-07 17:25:12.479257
    End Time: 2019-01-07 23:34:42.471545
    Elapsed Time: 369 Minutes and 29 Seconds
    Average Speed in MBytes/Second: 34.64
    Average Speed in GBytes/Minute: 2.03
    Average Speed in GBytes/Hour: 121.78
    # of chunks with the same 8192 byte chunk hash: 24720979
    Chunk Size in Bytes: 8192
    File Path for Recording Hashes: S:\Temp\ISO_Files_E_Drive_8192.hashes
    Total objects processed: 1852
    Total Bytes processed: 805,211,005,425
    Total MBytes processed: 767,909 Megabytes (Approx.)
    Total GBytes processed: 749.91 Gigabytes (Approx.)
    Minimum Gigabytes of duplicate data: 94.3 Gigabytes (Approx.)
    Total Chunks in Scope: 98292359
    Total objects not meeting chunk threshold: 509
    Total Data Path Issues Encountered: 0

**---End Example Input/Output---**

## Features

* Report on duplicate chunks of data for a given path via locally addressable paths/mounts or UNC locations

#### Argument 1 - Data Path for analysis
**Name:** folder_path
**Type: **`String`
**Default:** No Default Value

This argument supplies which path will be scanned.
###### e.g. python PyDupeStats.py "\\us-namespace\finance\payroll"

#### Argument 2 - Chunk size used for inspection of similarities
**Name:** chunk_size
**Type:** `Integer`
**Default:** No Default Value

- This argument sets the scope at which the tool will work from a file buffering and chunk analysis perspective.
###### 	e.g. python PyDupeStats.py "\\us-namespace\finance\payroll" 16384
- Keep in mind that the smaller the chunk size, the larger the memory footprint and the longer it will take to provide results.

## Contributing

This tool is pretty simple but is not without its shortcomings; all contributions are welcomed.

Aside from working on the random **TODO:** and enhancing the performance of the tool in the short term, I would like to see duplication assessment capabilities beyond that of rudimentary file layer access. For example, analyzing file constructs which could provide additional context for where an offset should start, or varying chunk length may be more appropriate. Additionally, adding support for additional interfaces such as S3 object storage, 

I welcome all feedback and contributions.


## Links

- Project homepage: https://github.com/Kentix/PyDupeStats/
- Repository: https://github.com/Kentix/PyDupeStats/
- Issue tracker: https://github.com/Kentix/PyDupeStats/issues

## License

The code in this project is licensed under the MIT license.