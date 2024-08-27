# Multiplication by Successive Additions - SAM in Python
![GitHub repo size](https://img.shields.io/github/repo-size/joaosnet/SAMPython?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/joaosnet/SAMPython?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/joaosnet/SAMPython?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/joaosnet/SAMPython?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/joaosnet/SAMPython?style=for-the-badge)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/joaosnet/SAMPython/blob/master/README.pt-br.md)

## Skills Developed
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/VHDL-00599C?style=for-the-badge&logo=vhdl&logoColor=white"/> <img src="https://img.shields.io/badge/ModelSim-00599C?style=for-the-badge&logo=ModelSim&logoColor=white"/> <img src="https://img.shields.io/badge/Quartus-00599C?style=for-the-badge&logo=Quartus&logoColor=white"/> <img src="https://img.shields.io/badge/Poetry-%233B82F6.svg?style=for-the-badge&logo=poetry&logoColor=0B3D8D" /> <img src="https://img.shields.io/badge/MyHDL-00599C?style=for-the-badge&logo=Quartus&logoColor=white"/>

## Introduction

### Digital System Implementation

This project implements a digital system that executes an algorithm using the BO+BC (Operational Block + Control Block) model. The system performs multiplication through repeated addition and subtraction operations.

### Features

- Implements a multiplication algorithm using a single adder/subtractor for cost efficiency
- Uses the BO+BC model for system design
- 4-bit input and output capabilities

### System Specifications

#### Inputs:

- Reset
- Clock (ck)
- entA (4 bits)
- entB (4 bits)

#### Outputs:

- mult (4 bits)
- pronto (ready signal)

#### States:

- Initial state (after reset)
- Wait state (while B = 0)
- Multiplication state (while A ≠ 0)
- Final state (when pronto = 1)

### Algorithm

The system implements the following algorithm:

```python
begin
pronto ← 0
A ← entA
B ← entB
P ← 0
If B ≠ 0 then
    While A ≠ 0 do
        begin
        P ← P + B
        A ← A - 1
        end
mult ← P
pronto ← 1
end
```

This algorithm performs multiplication through repeated addition, using a single adder/subtractor for both P+B and A-1 operations.

### Implementation Details

The system uses a shared adder/subtractor for P+B and A-1 operations, performing each operation in a separate clock cycle for optimal resource utilization.

## FSM - Finite State Machine

<img src="screenshots/fsm.png"/>

## Output

<img src="screenshots/output.png"/>


## How to Use

1. Clone this repository
2. Install the dependencies with [poetry](https://python-poetry.org/docs/#installation)
3. in folder `SAMPython` run the command 
``` bash 
poetry install
```
4. Run the command 
```bash
poetry shell 
python main.py
```



## 🤝 Contributing to Multiplication by Successive Additions - SAM

<table>
  <tr>
    <td align="center">
      <a href="https://www.instagram.com/jaonativi/" title="Desenvolvedor Backend">
        <img src="https://avatars.githubusercontent.com/u/87316339?v=4" width="100px;" alt="Foto do João Natividade no GitHub"/><br>
        <sub>
          <b>João Natividade</b>
        </sub>
      </a>
    </td>
  </tr>
</table>
