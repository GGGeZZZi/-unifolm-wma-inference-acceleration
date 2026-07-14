# 🚀 UnifoLM-WMA-0 Inference Acceleration

> 🏆 **ASC26 世界大学生超级计算机竞赛 二等奖** | **7.77× inference speedup**

Achieving 7.77× inference speedup for Unitree's humanoid robot 
world model through 6 systematic optimization techniques.

![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![CUDA](https://img.shields.io/badge/CUDA-12.4-green.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-2.4-orange.svg)
![ASC26](https://img.shields.io/badge/ASC26-2nd_Prize-gold.svg)

## 🏆 About

This project was developed by **Team Zero Point** from 
**Chongqing University of Posts and Telecommunications (CQUPT)** 
for the **ASC26 World Student Supercomputer Challenge (2026)**, 
where we won the **2nd Prize (二等奖)**.

We achieved a **7.77× inference speedup** on Unitree's UnifoLM-WMA-0 
world model for humanoid robots, while maintaining PSNR ≥ 25.

## 📊 Performance Results

| Optimization | Speedup | Cumulative Time |
|---|---|---|
| Baseline (50-step DDIM, FP32) | 1.00× | 588.42s |
| + Sampling Step Reduction (50→20) | 2.50× | 235.37s |
| + Kernel Fusion | 1.33× | 176.53s |
| + Asynchronous Pipeline | 1.18× | 150.05s |
| + Mixed Precision (FP16) | 1.43× | 105.04s |
| + KV Cache + Sparse Attention | 1.25× | 84.03s |
| + CUDA Graph Capture | 1.11× | **75.68s** |
| **Total** | **7.77×** | **75.68s** |

## 🛠️ Optimization Techniques

1. **Algorithmic**: DDIM step reduction, sparse temporal attention
2. **System-level**: Asynchronous pipeline, CUDA streams
3. **Hardware-aware**: FP16 mixed precision, Tensor Core
4. **Architectural**: KV cache, CUDA Graph capture
5. **Kernel-level**: Custom fused CUDA kernels

## 👥 Team Zero Point (CQUPT)

- **Ni Yankuo** (Team Lead / Project Coordination)
- **Wang Yujie** (Performance Analysis)
- **Guo Xiangjun** (Core Software Development)
- **Zhou Chenyang** (Technical Proposal)
- **Zhu Kangrui** (Repository Management)

Advisor: **Wu Hong**

## 📄 Documentation

- 📑 [ASC26 Competition Proposal](paper/ASC26_Proposal.pdf)
- 📝 [Project Journal](docs/JOURNAL.md)
- 📊 Performance Benchmarks (coming soon)

## 📫 Contact

📧 your.email@cqupt.edu.cn

## 📄 License

Apache License 2.0
