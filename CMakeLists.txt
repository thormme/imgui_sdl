cmake_minimum_required(VERSION 3.1)

project(main)

if (NOT EXISTS "${CMAKE_BINARY_DIR}/conan.cmake")
    message(STATUS "Downloading conan.cmake from https://github.com/conan-io/cmake-conan")
    file(DOWNLOAD
        "https://raw.githubusercontent.com/conan-io/cmake-conan/v0.8/conan.cmake"
        "${CMAKE_BINARY_DIR}/conan.cmake"
        EXPECTED_MD5 58bc519cadc890b5c33235defadc1176)
endif ()
include(${CMAKE_BINARY_DIR}/conan.cmake)

find_program(CONAN_CMD conan)
if(NOT CONAN_CMD AND CONAN_REQUIRED)
    message(FATAL_ERROR "Conan executable not found!")
endif()


conan_cmake_run(
    CONANFILE conanfile.py
    BASIC_SETUP CMAKE_TARGETS
    BUILD missing
)
conan_basic_setup()

aux_source_directory(. SRC_LIST)
add_executable(${PROJECT_NAME} ${SRC_LIST})

#include_directories(.)
#add_definitions(-DIMGDIR="../img/")

# C++17
#add_compile_options(-std=c++17) # does not work on macOS
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14")



target_link_libraries(${PROJECT_NAME} LINK_PUBLIC
    ${CONAN_LIBS_SDL2}
    ${CONAN_LIBS_IMGUI}
)
