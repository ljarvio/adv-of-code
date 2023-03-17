#!/bin/bash
create_tree() {
    # create tree based on what elf 'saw' when browsing (=input data)
    # keep track where dirs and files should be created as 
    # `cd` does not work with subshell
    basedir='.'
    while read -r cmd; do
        p1=$(echo "${cmd}" | cut -d" " -f1)
        if [[ $p1 == \$ ]]; then
            # this is a mkdir -command, sanitize: '$ cd foo' -> 'cd foo'
            c=$(echo $cmd | sed 's/^\$ //g')
            if [[ $(echo $c | cut -d" " -f1) == "cd" ]]; then
                basedir=$basedir/$(echo $c | cut -d" " -f2)
                #echo "read in '$cmd', basedir is now: '$basedir'"
            fi
        elif [[ $p1 =~ ^[0-9]+ ]]; then
            # insert file size as content of file to be read in later
            p2=$(echo "$cmd" | cut -d" " -f2)
            #echo "read in '$cmd', executing: 'echo $p1 > $p2'"
            echo $p1 > ${basedir}/$p2
        elif [[ $p1 == "dir" ]]; then
            # see directory -> make that directory
            p2=$(echo "$cmd" | cut -d" " -f2)
            newdir=${basedir}/${p2}
            #echo "read in '$cmd', executing: 'mkdir $newdir'"
            eval "mkdir $newdir"
        fi
    done < $1 
}

calc_size() {
    for d in $(find . -type d); do
        d_size=0
        for i in $(find $d -type f); do 
            s=$(cat $i)
            d_size=$(($d_size+$s))
        done
        echo "$d directory size is $d_size"
    done | awk '{if($NF<100000){sum+=$NF}} END{print sum}'
}

calc_curr_usage() {
        d_size=0
        for i in $(find . -type f); do 
            s=$(cat $i)
            d_size=$(($d_size+$s))
        done
        echo $d_size
}

calc_dir_sizes() {
    for d in $(find . -type d); do
        d_size=0
        for i in $(find $d -type f); do 
            s=$(cat $i)
            d_size=$(($d_size+$s))
        done
        echo "$d_size for directory $d"
    # list all dirs ascending in size, take 1st that exceeds limit
    done | sort -n | awk -v limit=$1 '$1 > limit  {print $1}' | head -1
}

free_up_required() {
    max_allowed_usage=40000000
    current_usage=$(calc_curr_usage)
    free_up=$(($current_usage - $max_allowed_usage))
    echo $free_up
}

create_tree ~/src/adv-of-code/2022/7/testdata.txt
echo "Part 1: Total size of <100k dirs: $(calc_size)"
echo "Part 2: dir size to be removed: $(calc_dir_sizes $(free_up_required))"