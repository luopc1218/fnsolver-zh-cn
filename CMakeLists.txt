cmake_minimum_required(VERSION 3.28)
project(fnsolver
    VERSION 1.1.1
    DESCRIPTION "《异度神剑X》边境网络布局求解工具（简体中文版）"
    LANGUAGES CXX
    HOMEPAGE_URL "https://github.com/luopc1218/fnsolver-zh-cn"
)
set(PROJECT_DISPLAY_NAME "FnSolver 简体中文版")
set(PROJECT_AUTHOR "beta382")
set(PROJECT_ORGANIZATION_NAME "${PROJECT_AUTHOR}")
set(CMAKE_CXX_STANDARD 20)

include_directories(${CMAKE_CURRENT_SOURCE_DIR} ${CMAKE_CURRENT_BINARY_DIR})
add_subdirectory(fnsolver)

option(BUILD_PACKAGE Off)
if (BUILD_PACKAGE)
  add_subdirectory(install)
endif ()
