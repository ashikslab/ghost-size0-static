cmake_minimum_required(VERSION 3.14)
project(testCurlPP LANGUAGES CXX)
set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(FindPkgConfig)
pkg_check_modules(CURLPP REQUIRED curlpp)

add_executable(fetch_from_ghost
  fetch_from_ghost.cc
)

add_executable(parse_posts
  parse_posts.cc
)

add_executable(parse_pages
  parse_pages.cc
)

target_link_libraries(fetch_from_ghost
    ${CURLPP_LDFLAGS}
    )
