#include <rapidjson/document.h>
#include <rapidjson/filereadstream.h>

#include <cstdio>
#include <fstream>
#include <iostream>
#include <map>

int main()
{
	// Open the file
	FILE* fp = fopen("posts.json", "rb");
	// Check if the file was opened successfully
	if (!fp) {
		std::cerr << "Error: unable to open file"
				<< std::endl;
		return -1;
	}

	// Read the file 
	char readBuffer[65536];
	rapidjson::FileReadStream is(fp, readBuffer, sizeof(readBuffer));

	// Parse the JSON document
	rapidjson::Document doc;
	doc.ParseStream(is);

	// Check if the document is valid
	if (doc.HasParseError()) {
		std::cerr << "Error: failed to parse JSON document"
				<< std::endl;
		fclose(fp);
		return 1;
	}

	// Close the file
	fclose(fp);

	if (doc.HasMember("posts")
            && doc["posts"].IsArray()) {
          const rapidjson::Value& posts = doc["posts"];
          system("mkdir content");
          for (rapidjson::SizeType i = 0; i < posts.Size();
               i++) {
            if (posts[i].IsObject()) {
            auto post = posts[i].GetObject();
            std::string postid = post["id"].GetString();
            std::cout<< postid <<": "<<post["title"].GetString() <<std::endl;
            char filename[64];
            snprintf(filename, sizeof filename, "content/post-%s.html", postid.c_str());
            std::ofstream post_file;
            post_file.open(filename);
            post_file << "<html>";
            post_file << post["html"].GetString();
			post_file <<"<title>";
			post_file << post["title"].GetString();
			post_file <<"</title>";
            post_file <<"</html>";
            post_file.close();   
          }
	}

	return 0;
}
}
