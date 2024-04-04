<a name="readme-top"></a>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Using decorators such as line_profiler or memory_profiler to find CPU bound or memory bound bottleneck is very effective.
Yet to run profiling, this requires to put `@profile` decorator above the functions that we want to profile its performance.
This can become cumbersome and inefficient when we have large code base with multiple functions to profile.

Approaches:
1. Passing function names as argumend in CLI
-  pass function names as arguments in command line
-  without putting decorator on top of those functions, it will run profiling

2. Put decorator as you want, but wrap decorators with something that disables.


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

<p align="right">(<a href="#readme-top">back to top</a>)</p>