#include <pybind11/pybind11.h>
#include <pybind11/stl.h> // Allows conversion between Python lists/dicts and C++
#include <map>
#include <string>
#include <vector>
#include <cstdlib> // For rand()
using namespace std;
namespace py = pybind11;

class RaList {
private:
    // A map is like a Python dict: {"apple": "fruit", "car": "vehicle"}
    map< string, string> dictionary; 

    // A separate list of keys just to pick random words fast
    vector<string> keys;


public:
    // Constructor (Startup)
    RaList() { 

    }

    // Function 1: Add a word to the database
    void add_words(vector <string> values) {
        for(int i = 0; i < values.size(); i++)
            keys.push_back(values[i]);
    }

    // Function 2: Get a random word
    string get_random_word() {
        if (keys.empty()) {
            return {"No Words :'("};
        }
        // Pick a random index
        int random_index = rand() % keys.size();
        string random_key = keys[random_index];
        
        // Return word
        return random_key;
    }
    
    // Function 3: Get definition of specific word
    /*
        string get_definition(string key) {
            if (dictionary.count(key)) {
                return dictionary[key];
            }
            return "Word not found";
        }
    */
};

// --- PART 3: THE MENU (The Binding) ---
// This is the ONLY part Python sees.
// "lexicon_engine" MUST match the name in setup.py
PYBIND11_MODULE(lexicon_engine, m) {
    
    // We are telling Python: "There is a class called 'RaList'"
    py::class_<RaList>(m, "RaList")
        .def(py::init<>()) // Expose the constructor
        .def("add_words", &RaList::add_words) // Expose add_word function
        .def("get_random_word", &RaList::get_random_word);
        //.def("get_definition", &RaList::get_definition);
}