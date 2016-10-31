find . -name "*.bz2" | xargs -P 5 -I fileName sh -c 'bzip2 -d "fileName" ;rm "filename"';
