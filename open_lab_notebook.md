18.06-2018 - 23.06.2018
  - fixed ascii errors, when calling for input using psychopy gui -> see troubleshooting docs
    -> Umlaute used by subjects used to break save function, but declaring system encoding as utf-8
      (https://stackoverflow.com/questions/28657010/dangers-of-sys-setdefaultencodingutf-8) solved this
       (should only be necessary in python2.7)
