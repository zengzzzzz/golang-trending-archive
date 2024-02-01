# Golang Trending Archive

Welcome to the Golang Trending Archive! This project aims to track and archive historical GitHub trending projects related to Go (Golang). <br>
This reposity reference from [aneasystone/github-trending](https://github.com/aneasystone/github-trending).

## Table of Contents

- [Golang Trending Archive](#golang-trending-archive)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Implementation](#implementation)
  - [Getting Started](#getting-started)
  - [All language](#all-language)
  - [Go](#go)
  - [Python](#python)
  - [Javascript](#javascript)
  - [C](#c)
  - [C++](#c-1)
  - [Typescript](#typescript)

## Introduction

The Golang Trending Archive is a project dedicated to preserving the historical records of trending GitHub projects related to the Go programming language. As GitHub's trending list is constantly changing, this repository helps in maintaining a historical archive of these projects.

## Features

- Archive of historical GitHub trending projects related to Go.
- Regular updates using GitHub Actions.
- No language restrictions, removing the Chinese query limitation.
- Monthly scheduled archiving tasks.

## Implementation

The main implementation of this project involves the following steps:

1. **Scraping GitHub Trending:** We use web scraping techniques to request and parse GitHub's trending page for Go projects. This allows us to extract information about trending projects.

2. **Data Storage:** Extracted data is stored in a structured format, such as md files, to maintain historical records.

3. **GitHub Actions:** We utilize GitHub Actions to automate the process of updating the archive on a regular basis. You can find the workflow configuration in the `.github/workflows` directory.

## Getting Started

To get started with the Golang Trending Archive, follow these steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/zengzzzzz/golang-trending-archive.git

# Daily Trending

