# Distributed Streaming Data Sharing Manager (DSSM)

This repository contains a Python interface for the Distributed Streaming Data Sharing Manager (DSSM) 

## Requirements
The Python interface requires an executable DSSM environment. You can find the instructions under [link follows](URL).

## Installing

To use the Python interface, the following library must be installed.

```bash
pip install sysv-ipc
```

## Dataclass
The Python interface makes it possible to exchange data between different processes, both in Python and in C.
To define which data is exchanged, the dataclass must first be defined. An example can be found in the ```/sample``` folder.

The corresponding dataclass of the C++ example is the ```/sample/ini_ssm.py``` class.


## Sample

The sample programs included can be found can be found in the project. These are defined in such a way that data can be exchanged between Python and C/C++.

This was tested with the SSM C++ sample that can be found in the corresponding project in the ```/sample/Cpp_sample``` folder.
The following shows how data can be exchanged between Python and C++.

For the data exchange to work, the coordinator must be executed as in DSSM.

```bash
ssm-coordinator
```

### C++ write data

In this example, data is sent from the C++ example and read by Python.

#### C++ write
```bash
./samples/Cpp_Sample/ssmWriteSample 
```

#### Python read
```bash
python3 sample/read_sample.py
```

### Python write data

In this example, data is sent from the Python example and read by C++ and Python.

#### Python write

```bash
python3 sample/write_sample.py
```

#### Python read
```bash
python3 sample/read_sample.py
```

#### C++ read
```bash
./samples/Cpp_Sample/ssmReadSample
```




