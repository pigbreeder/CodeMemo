#pragma once
#include <iostream>
#include <string>

#ifdef __ANDROID__
#include <android/log.h>
#define  LOGI(...)  __android_log_print(ANDROID_LOG_INFO,LOG_TAG,__VA_ARGS__)
#define  LOGE(...)  __android_log_print(ANDROID_LOG_ERROR,LOG_TAG,__VA_ARGS__)
#endif

using namespace std;

namespace ASDF {

    class Log {
    public:
        static const int ALL = -1;
        static const int RCDEBUG = 0;
        static const int WARNING = 1;
        static const int INFO = 2;
        static const int ERROR = 3;
        static const int NONE = 4;

    private:
        Log(void);

    public:
        ~Log(void);
        static Log& Instance() { return s_instance; }
        ostream& Out() { return *m_out; }
        // get current time
        long Time() const;
        // return the time in this duration
        double Time(long begin, long end) const {
          return (double)(end - begin) / m_time_unit;
        }
        bool SetOut(const string &file);
        void SetTimeUnit(const int unit) { m_time_unit = unit; }
        void SetVerbose(const int verbose) { m_verbose = verbose; }
        int GetVerbose() { return m_verbose; }
        bool IsVerbose(const int level) { return level >= m_verbose; }
        void Verbose(const int level, const string &message) {
          if (level >= m_verbose){
            *m_out << message << endl;
          }
#ifdef __ANDROID__
          LOGI("youdao_nmt:%s", message.c_str());
#endif
        }
        void Error(const string& message) {
          Verbose(ERROR, message);
        }
        void Info(const string& message) {
          Verbose(INFO, message);
        }
        void Debug(const string& message) {
          Verbose(RCDEBUG, message);
        }
        void Warning(const string& message) {
          Verbose(WARNING, message);
        }
    private:
        static Log s_instance;
        ostream * m_out; // output stream
        string m_out_file;  // file to store the log
        int m_time_unit;  // default = 1000, which means seconds
        int m_verbose;  // verbose level, default = INFO
    };

};
