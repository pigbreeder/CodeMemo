#include <ctime>
#include <fstream>

#include "Log.hpp"

namespace ASDF {
    Log Log::s_instance;

    Log::Log(void) {
      m_verbose = ERROR;
      m_out = &std::cerr;
      m_time_unit = CLOCKS_PER_SEC;
    }

    Log::~Log(void) {
      if (m_out_file != "") {
        ((ofstream *)m_out)->close();
        delete m_out;
      }
    }

    bool Log::SetOut(const string &file) {
      m_out_file = file;
      m_out = new ofstream(m_out_file.c_str());
      if (((ofstream *) m_out)->good()) {
        cerr << "Error: fail to init output of log by file \""
             << m_out_file << "\"" << endl;
        delete m_out;
        return false;
      }
      return true;
    }

    long Log::Time() const {
      return (long)clock();
    }

};
