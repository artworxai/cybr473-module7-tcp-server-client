# CYBR 473: Violent Python - Module 7 Assignment

**Author:** Dana Willis Martinez  
**Date:** October 18, 2026  
**Course:** CYBR 473 - Violent Python (University of Arizona)

## Overview
This repository contains standalone Python scripts demonstrating TCP socket programming and cryptographic data integrity checks.

- **Assignment 1/2 (TCP Server):** Listens on Port 5555, accepts incoming connections, receives messages, computes an MD5 cryptographic hash, and responds with the hex digest[cite: 3].
- **Assignment 2/2 (TCP Client):** Connects to the TCP server on Port 5555, sends 10 differing messages sequentially, and receives the MD5 hex digest responses[cite: 4].

## Files Included
* `martinezD_WK7_script_01.py` - TCP Server Script[cite: 3]
* `martinezD_WK7_script_02.py` - TCP Client Script[cite: 4]

## How to Run
1. **Start the Server:** `python martinezD_WK7_script_01.py`[cite: 3]
2. **Start the Client:** `python martinezD_WK7_script_02.py`[cite: 4]
