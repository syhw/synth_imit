for voice in `say -v? | cut -d" " -f1`;
do echo $voice
for file in *.txt;
    do say -v $voice -f $file -o ${voice}_${file%.*}.aif
done;
done
