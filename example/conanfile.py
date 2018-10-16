from conans import ConanFile, CMake

class StrifeConan(ConanFile):
   settings = "os", "compiler", "build_type", "arch"
   requires = \
        "sdl2/2.0.8@bincrafters/stable", \
        "sdl2_image/2.0.3@bincrafters/stable", \
        "imgui/1.62@bincrafters/stable"

   generators = "cmake"
