
Andrii Alexieiev
================
------------------
Software Developer
------------------

.. class:: mid

  :tel:`+43 160 4345920` | akari@taisei-project.org | GitHub: :github:`Akaricchi` | Mörfelden-Walldorf, Germany

----

Hobbyist programmer from Ukraine with over 10 years of informal experience, particularly in game development and 
modding, as well as in contributing to and maintaining various open source software projects.

Skills
------

* **Spoken languages**:
    
    * Ukrainian (native)
    * Russian (native)
    * English (fluent)

* **Programming languages**:

    * **Primary expertise**: C
    * **Secondary expertise**: Python
    * **Familiarity**: Bash, C++, JavaScript, Lua, Java, various others.

* **Operating systems**: Linux

* **Graphics programming**: OpenGL 3.3+, GLSL

* **Build systems**: Meson, CMake, GNU Make

* **Version control**: git

* **Debugging**: gdb, prof, strace, etc.

* **Documentation**: Doxygen, docutils

* **Other software**: nginx, Blender, Krita, GIMP, SPIR-V tools


Open Source involvement
-----------------------

.. project:: Taisei Project
  :url: https://taisei-project.org/
  :role: Contributor (2011 - 2013); Lead Developer (2017 - present)
 
  A free and open source Japanese-style "bullet hell" (Danmaku_) top-down shooter; a fangame of the `Touhou Project`_ 
  series. Original engine built with SDL, with a custom OpenGL 3.3 renderer. Written in C (GNU C11), with tooling 
  written in Python. Runs on any modern desktop OS and in the browser (via Emscripten_).

  * (Re-)wrote most of the engine, including but not limited to the renderer, audio, virtual filesystem, replay, live 
    reloading, and threaded asset loading subsystems. 
  * Designed and implemented a system for asynchronous programming of game logic and stages in C based on stackful 
    coroutines, with a macro-powered DSL. 
  * Designed and implemented a lot of the gameplay mechanics, stages, bullet patterns, and special effects. 


.. project:: Koishi
  :url: https://github.com/taisei-project/koishi
  :role: Lead Developer (2019 - present)
  
  A small, decently portable C11 library that implements asymmetric stackful coroutines (similar to Lua's coroutines, 
  but for native code). Supports many operating systems and CPU architectures. Modular design, can use boost.context 
  assembly routines, POSIX ucontext, Windows fibers, longjmp, Emscripten fibers, etc.

  Designed for use in `Taisei Project`_, but is general enough to be useful elsewhere.


.. project:: Emscripten
  :url: https://emscripten.org/
  :role: Contributor (2019 - present; intermittent)

  An LLVM-based suite of tools for compiling C/C++ applications to WebAssembly_, as well as a runtime to run them in 
  the browser.

  * Designed and implemented the Fibers_ API and runtime, a low-level context-switching primitive similar to POSIX 
    ucontext, based on Asyncify_.
  * Found and squished various random bugs in the runtime.


.. project:: Meson
  :url: https://mesonbuild.com/
  :role: Contributor (2017 - present; intermittent)

  A declarative build system written in Python, meant to be as fast and user-friendly as possible.

  `Taisei Project`_ uses Meson extensively.

  * I often test unstable revisions; identify, report, and fix bugs and regressions.

  * Proposed and implemented some minor features for my project's needs.

  * I maintain custom Meson build definitions for most of `Taisei Project`_'s dependencies, including SDL2_, 
    `Basis Universal`_, `SPIRV-Tools`_, glslang_, shaderc_, `SPIRV-Cross`_, libpng_, libwebp_, Freetype_, libzip_, 
    zlib_, ogg_, opus_, opusfile_


.. project:: RocketMinsta
  :url: https://github.com/kasymovga/RocketMinsta
  :role: Lead Developer (2011 - 2017)
    
  A formerly popular multi-feature mod for Nexuiz_, a defunct open source first-person arena shooter game. Features new 
  game types, bug fixes, server administration tools, updated graphics, Xonotic_ backports, and more. Written in a 
  dialect of QuakeC, an interpreted language for Quake 1-based engines.


.. project:: DarkPlacesRM
  :url: https://github.com/kasymovga/DarkPlacesRM
  :role: Fork Developer (2015 - 2017)
 
  A fork of the DarkPlaces engine which powers Nexuiz_ and Xonotic_. Features RocketMinsta_-specific extensions and 
  compatibility fixes.

  
.. project:: rmqcc
  :url: https://github.com/kasymovga/rmqcc
  :role: Fork Developer (2016 - 2017)

  A fork of fteqcc_, a QuakeC compiler, used to compile the RocketMinsta_ source code. Features various language 
  extensions and fixes. 


.. project:: ųz
  :url: https://github.com/Akaricchi/muz
  :role: Lead Developer (2015 - 2016)

  A beatmania-style rhythm game written in Python with a pygame frontend. Can load osu!mania beatmaps.


.. project:: This resume
  :url: https://akaricchi.github.io/resume
  :role: Author (2022 - present)
  
  An up to date HTML version of this resume is available at https://akaricchi.github.io/resume
  
  You have revision :revision:`.`, built on :date:`%b %d %H:%M UTC`
  
  The source code is available at https://github.com/Akaricchi/resume


.. _Asyncify: https://kripken.github.io/blog/wasm/2019/07/16/asyncify.html
.. _Basis Universal: https://github.com/taisei-project/basis_universal
.. _Danmaku: https://en.wikipedia.org/wiki/Danmaku
.. _Fibers: https://emscripten.org/docs/api_reference/fiber.h.html
.. _Freetype: https://github.com/taisei-project/freetype2/tree/meson-2.10.1
.. _Nexuiz: http://www.alientrap.com/games/nexuiz/
.. _SDL2: https://github.com/taisei-project/SDL/tree/meson-2.0.20
.. _SPIRV-Cross: https://github.com/taisei-project/SPIRV-Cross/tree/meson-2021.01.15
.. _SPIRV-Tools: https://github.com/taisei-project/SPIRV-Tools/tree/meson-2020.7
.. _Touhou Project: https://en.wikipedia.org/wiki/Touhou_Project
.. _Xonotic: https://xonotic.org/
.. _fteqcc: https://www.fteqcc.org/
.. _glslang: https://github.com/taisei-project/glslang/tree/meson-11.2.0
.. _libpng: https://github.com/taisei-project/libpng/tree/meson-1.6.37
.. _libwebp: https://github.com/taisei-project/libwebp/tree/meson-1.2.0
.. _libzip: https://github.com/taisei-project/libzip/tree/meson-1.7.3.142
.. _ogg: https://github.com/taisei-project/ogg/tree/meson-1.3.4
.. _opus: https://github.com/taisei-project/opus/tree/meson-1.3.1
.. _opusfile: https://github.com/taisei-project/opusfile/tree/meson-0.12
.. _shaderc: https://github.com/taisei-project/shaderc/tree/meson-2020.5
.. _zlib: https://github.com/taisei-project/zlib/tree/meson-1.2.11
.. _WebAssembly: https://webassembly.org/

.. vim: tw=120 spell
