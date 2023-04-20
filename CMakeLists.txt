# CmakeLists for building python bindings
cmake_minimum_required(VERSION 3.0)

project(llamapy)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

set(GGML_USE_ACCELERATE 1)
find_package(pybind11 CONFIG REQUIRED)

add_subdirectory(llama.cpp)
pybind11_add_module(llamapy MODULE llamapy/llama2.cpp llamapy/llama_wrapper.cpp llamapy/llama_wrapper.h)
target_include_directories(llamapy PRIVATE llama.cpp)
target_link_libraries(llamapy PRIVATE pybind11::module pybind11::lto pybind11::windows_extras llama)
add_link_options(-no_fixup_chains)

if(NOT MSVC AND NOT ${CMAKE_BUILD_TYPE} MATCHES Debug|RelWithDebInfo)
    # Strip unnecessary sections of the binary on Linux/macOS
    pybind11_strip(llamapy)
endif()

set_target_properties(llamapy PROPERTIES CXX_VISIBILITY_PRESET "hidden"
    CUDA_VISIBILITY_PRESET "hidden")

install(TARGETS llamapy DESTINATION llamapy)
