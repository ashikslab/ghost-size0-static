
#include <sstream>
#include <fstream>

#include <cstdlib>
#include <cstring>

#include <curlpp/cURLpp.hpp>
#include <curlpp/Easy.hpp>
#include <curlpp/Options.hpp>
#include <curlpp/Exception.hpp>

#define DEBUG_LEVEL -1

int main(int argc, char *argv[])
{
  if(argc != 3) {
    std::cerr<< argv[0] << ": Usage: " << " apiurl contentkey" << std::endl;
    return -1;
  }

  char url_posts[128], url_pages[128];

  snprintf(url_posts, sizeof url_posts, "%s/ghost/api/content/posts/?key=%s&limit=all", argv[1], argv[2]);
  snprintf(url_pages, sizeof url_pages, "%s/ghost/api/content/pages/?key=%s", argv[1], argv[2]);  
  if (DEBUG_LEVEL > 0) std::cout<<"urls to fetch are "<<std::endl<<url_posts<<std::endl<<url_pages<<std::endl;
  
  try {
    curlpp::Cleanup cleaner;
    curlpp::Easy request1, request2;

    // Setting the URL to retrive.
    request1.setOpt(new curlpp::options::Url(url_posts));

    if (DEBUG_LEVEL > 0) std::cout << request1 << std::endl;

    std::ofstream outfile;
    outfile.open ("posts.json");
    outfile << curlpp::options::Url(url_posts) << std::endl;
    outfile.close();

    request2.setOpt(new curlpp::options::Url(url_pages));
    if (DEBUG_LEVEL > 0) std::cout << request2 << std::endl;

    outfile.open ("pages.json");
    outfile << curlpp::options::Url(url_pages) << std::endl;
    outfile.close();
    
    

    return EXIT_SUCCESS;
  }
  catch ( curlpp::LogicError & e ) {
    if (DEBUG_LEVEL > 0) std::cout << e.what() << std::endl;
  }
  catch ( curlpp::RuntimeError & e ) {
    if (DEBUG_LEVEL > 0) std::cout << e.what() << std::endl;
  }

  return EXIT_FAILURE;
}
