from conans import ConanFile, CMake

class ConanComponent(ConanFile):
    name = "log4cplus"
    version = "1.2.0-RC4"
    url = "https://github.com/Kretsch0/log4cplus"
    license = "Apache License V2.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports = "*"
    
    def requirements(self):
        pass
        
    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake "%s/%s" %s -DCMAKE_INSTALL_PREFIX=install -DLOG4CPLUS_ENABLE_DECORATED_LIBRARY_NAME=OFF -DUNICODE=OFF' % (self.conanfile_directory, self.name, cmake.command_line))
        self.run('cmake --build . %s --target install' % cmake.build_config)
        
    def package(self):
        self.copy("*.h", dst="include/" + self.name, src="install/include/" + self.name)
        self.copy("*.hxx", dst="include/" + self.name, src="install/include/" + self.name)
        self.copy("*.lib", dst="lib", src="install/lib/")
        self.copy("*.dll", dst="bin", src="install/bin/")
        
    def package_info(self):
        #these are the names of the libs that other components should link with
        self.cpp_info.libs = [self.name]

    def source(self):
        self.run("git clone https://github.com/log4cplus/log4cplus.git")
        self.run("cd log4cplus && git checkout --no-track -b Branch_REL_1_2_0-RC4 REL_1_2_0-RC4")