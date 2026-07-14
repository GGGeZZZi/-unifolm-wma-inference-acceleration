# 🚀 ASC26 Zero Point: 双任务优化方案

> 🏆 **ASC26 世界大学生超级计算机竞赛 二等奖** (Two-Task Submission)
> 
> **任务 A**: 7.77× 推理加速 (Unitree World Model) | **任务 B**: 2.59× 模拟加速 (AMSS-NCKU 引力波)
> 
> CQUPT Team Zero Point · 5 个本科一二年级学生 · 从零开始

![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![CUDA](https://img.shields.io/badge/CUDA-12.4-green.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-2.4-orange.svg)
![MPI](https://img.shields.io/badge/MPI-Intel%20MPI-blue)
![Fortran](https://img.shields.io/badge/Fortran-77%2F90-purple)
![ASC26](https://img.shields.io/badge/ASC26-2nd%20Prize-gold)

## 🏆 About

This project was developed by **Team Zero Point** from **Chongqing University of Posts and Telecommunications (CQUPT)** for the **ASC26 World Student Supercomputer Challenge (2026)**, where we won the **2nd Prize (二等奖)**.

As a team of **5 undergraduate students (mostly freshmen/sophomores)** from the School of Electronic and Information Engineering, we tackled **two completely different HPC challenges** in a single competition, demonstrating both **breadth (AI + Classical HPC)** and **depth (7+ optimization techniques)**.

Our motto: **"From Zero, Everything"** - we started with curiosity, not experience.

## 🎯 Two-Task Achievement Summary

### 📊 Task A: UnifoLM-WMA-0 World Model (GPU Inference)
- **🏆 Application**: Humanoid robot "mental rehearsal" for Unitree's VLA system
- **⚡ Result**: **7.77× inference speedup** (588s → 75.68s)
- **🎯 Quality**: All 20 test samples pass PSNR ≥ 25 (avg 27.58)
- **🛠️ 6 techniques**: DDIM, Kernel Fusion, Async Pipeline, Mixed Precision, KV Cache, CUDA Graphs
- **💻 Hardware**: AMD EPYC 9754 + AMD W7900D GPU × 2

### 📊 Task B: AMSS-NCKU Numerical Relativity (CPU HPC)
- **🏆 Application**: GW150914 binary black hole merger simulation (LIGO/Nobel Prize 2017)
- **⚡ Result**: **2.59× speedup** (122min → 47min for 10s physical time)
- **🎯 Full-scale**: 1000s simulation in 32.8 hours (vs. 157+ hours original)
- **🛠️ Optimizations**: MPI 16-core, LTO compiler, process pinning, thread control
- **💻 Hardware**: Intel Xeon E5-2690 v3 (12 cores)
- **🔬 Research bonus**: Attempted CSAMR (2016 paper) - failed but valuable lessons

## 📈 Performance Results

### Task A: Cumulative Optimization Speedup

| Optimization | Speedup | Cumulative Time | PSNR |
|---|---|---|---|
| Baseline (50-step DDIM, FP32) | 1.00× | 588.42s | 27.71 |
| + DDIM Sampling Reduction (50→20) | 2.50× | 235.37s | 27.68 |
| + Kernel Fusion | 1.33× | 176.53s | 27.65 |
| + Asynchronous Pipeline (CUDA Streams) | 1.18× | 150.05s | 27.65 |
| + Mixed Precision (FP16 + Tensor Core) | 1.43× | 105.04s | 27.62 |
| + KV Cache + Sparse Attention | 1.25× | 84.03s | 27.60 |
| + CUDA Graph Capture | 1.11× | **75.68s** | **27.58** |
| **Total** | **7.77×** | **75.68s** | **-0.13 drop** |

### Task B: AMSS-NCKU Performance Comparison

| Configuration | Total Time | Evolution | Speedup |
|---|---|---|---|
| 4 cores (baseline) | 122 min | 94 min | 1.00× |
| 8 cores | 76 min | 48 min | 1.61× |
| 12 cores | 86 min | 56 min | 1.42× |
| **16 cores (optimal)** | **51 min** | **23 min** | **2.40×** |
| 24 cores (degraded) | 57 min | 29 min | 2.14× |
| **Final (16 cores + LTO + pinning)** | **47 min** | **29 min** | **2.59×** |

## 🛠️ Technical Highlights

### Task A: 6 Core Optimization Techniques
1. **Algorithmic**: DDIM step reduction (50→20), sparse temporal attention
2. **System**: Asynchronous pipeline with CUDA streams, prefetching
3. **Hardware-aware**: FP16 mixed precision, Tensor Core utilization
4. **Architectural**: KV cache with FIFO eviction, CUDA Graph capture
5. **Kernel-level**: Custom CUDA kernels (LayerNorm+GeLU+Residual fusion)
6. **Engineering**: PyTorch compile, channels_last memory format

### Task B: Classical HPC Techniques
- **MPI parallelization**: Optimal 16-core configuration
- **Compiler optimization**: -O2 -march=native -flto
- **Runtime tuning**: Process pinning, thread concurrency control
- **Algorithm exploration**: CSAMR attempt (learned from failure)

## 📊 Comprehensive Improvements Summary

| Metric | Task A Improvement | Task B Improvement |
|---|---|---|
| Total Time | -87% (7.77×) | -61% (2.59×) |
| GPU/CPU Utilization | 62% → 94% | Linear scaling |
| Memory Usage | -39.5% (24.3GB → 14.7GB) | Optimized |
| Quality | PSNR maintained | Constraint violation < 0.5 |
| Compliance | 100% (20/20 samples) | 100% (RMS < 1%) |

## 👥 Team Zero Point (CQUPT)

5 undergraduate students from the **School of Electronic and Information Engineering**:

| Name | Role | Responsibility |
|------|------|----------------|
| **Ni Yankuo** (倪彦阔) | **Team Lead** | Project coordination & technical roadmap |
| Wang Yujie | Performance Analyst | Benchmarking & optimization measurement |
| Guo Xiangjun | Core Developer | Architecture design & code review |
| Zhou Chenyang | Technical Writer | Proposal design & documentation |
| Zhu Kangrui | Repository Manager | Git operations & version control |

**Advisor**: Wu Hong

## 📚 Repository Structure
unifolm-wma-inference-acceleration/
├── README.md                    # This file
├── LICENSE                       # Apache 2.0
├── ASC1548-...pdf              # ASC26 Competition Proposal
├── paper/                        # (coming soon)
├── src/                          # Source code
│   ├── task_a_unifolm/          
│   │   ├── optimizations/       
│   │   │   ├── sampling.py      
│   │   │   ├── fused_kernels.cu
│   │   │   └── ...
│   │   └── inference/           
│   └── task_b_amss/             
├── benchmarks/                   
├── docs/                        
└── notebooks/                   


## 📖 Documentation

- 📑 [ASC26 Competition Proposal (93 pages)](ASC1548-8b9b01cf-3ce0-af82-7130-d6fedcb7a6c9.pdf)
- 📝 [Project Journal](docs/JOURNAL.md) (coming soon)
- 🏗️ [Architecture Overview](docs/architecture.md) (coming soon)
- 💡 [Lessons Learned](docs/lessons_learned.md) (coming soon)

## 🎓 Lessons Learned

### What Worked ✅
- **Systematic profiling first** - Nsight Systems revealed real bottlenecks
- **Layered optimizations** - Multiple techniques compound effectively
- **Quality preservation** - PSNR drop of only 0.13 across all 20 samples
- **Hardware adaptation** - Optimized for AMD GPU, not just NVIDIA

### What Didn't Work ❌ (But Taught Us)
- **CSAMR (Advanced Algorithm)**: 1 hour → 0.7s physical time on 16 cores
  - Lesson: "Advanced" algorithms need matching hardware (paper used 128+ cores)
- **-Os Size Optimization**: Slightly worse than -O2
  - Lesson: Numerical code benefits from -O2 + -flto
- **Intel MKL Replacement**: Performance degraded
  - Lesson: Not all workloads benefit from MKL (AMR ≠ dense linear algebra)
- **PGO (Profile-Guided Optimization)**: Compilation failed
  - Lesson: GCC 4.8.5 PGO support is limited

## 🔧 Reproducibility

### Task A
```bash
# Install dependencies
pip install torch==2.4.0 torchvision==0.19.0
pip install tensorrt==10.0 triton-inference-server==24.01

# Run benchmark
cd src/task_a_unifolm
python inference/benchmark.py --config configs/optimized.yaml
```
### Task  B
# Compile optimized version
cd src/task_b_amss
source compile/setup_env.sh
make -f compile/Makefile.asc26
```
# Submit job
qsub jobs/gw150914_1000s.pbs

📫 Contact
Team Zero Point, CQUPT

📧 Primary contact: Zhu kangrui 2498786739@qq.com
🏫 School of Electronic and Information Engineering
📍 Chongqing University of Posts and Telecommunications
📄 License
This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

🙏 Acknowledgments
CQUPT Supercomputing Center for providing AMD GPU cluster access
Unitree Robotics for the UnifoLM-WMA-0 model and competition
ASC26 Organizers for the competition platform
Advisor Wu Hong for guidance and support
All CQUPT faculty who supported our team
