#!/bin/bash
# Create by xsy
# Evaluate multiple model in one test file
#SBATCH -o log.eval.batch
#SBATCH -p mt_test
#SBATCH -N1
#SBATCH -n1
#SBATCH --cpus-per-task=1
#SBATCH --gres=gpu:1

curdir=`cd $(dirname $0);pwd`
now_time=`date '+%Y%m%d_%H%M%S'`
prefix="eval_batch"
output='.'
st=10000
ed=20000

usage(){
  echo "Usage:"
  #echo "Run in the same directory as tensor2tensor folder"
  echo "sh `basename $0`  -p problems -d data_dir -m model_dir -i test_file -o output -s start_model_index -t end_model_index  -S src_language -T target_language [-P prefix]"
  echo 'P:prefix, defined to distinguish your eval result'
  echo 'p:problems, which define in your work_dir/your.py'
  echo 'H:hparams, which define in your work_dir/your.py'
  echo 'd:data_dir, tensorflow gendata location'
  echo 'm:model_dir, model_dir'
  echo 'i:input,  test file'
  echo 'o:output, result output folder'
  echo 'Example:'
  echo "sh `basename $0` -p translate_en2cn -d en2cn_gendata -m model_folder/ -i test_file.sub.word -o /tmp/ -s 20000 -t 30000 -S en -T cn"
}

if [ $# -lt 10 ] ; then
    echo 'params not enough'
    usage
    exit 1
fi  

while getopts ":P:p:H:d:m:i:o:s:t:S:T:h" opt; do
  case $opt in
    P)
      prefix=$OPTARG ;;
    p)
      problems=$OPTARG ;;
    H)
      hparams=$OPTARG ;;
    d)
      data_dir=$OPTARG ;;
    m)
      model_dir=$OPTARG ;;
    i)
      test_file=$OPTARG ;;
    o)
      output=$OPTARG ;;      
    s)
      st=$OPTARG ;;
    t)
      ed=$OPTARG ;;  
    S)
      src_lan=$OPTARG ;;
    T)
      tgt_lan=$OPTARG ;;  
   \?)
      echo "Invalid option: -$OPTARG"; usage ; exit 1;;
  esac
done
# 正则变量/$ 不能加双引号
# if [[ "$newip" =~ ^([0-9]{1,3}.){3}[0-9]{1,3}$ ]];then
if [[ "$output" =~ /$ ]]; then
	output=${output%/*} 
fi

if [[ "$model_dir" =~ /$ ]]; then
	model_dir=${model_dir%/*} 
fi
while [ $st -le $ed ]; do

	file=${model_dir}/model.ckpt-${st}.index
	if [ ! -f "${file}" ]; then
	  echo "${file} NOT exist..."
	  sleep 100
	  continue
	fi
	sleep 5
	ckpt_path=${model_dir}/model.ckpt-${st}

	decode_from_file=${test_file}.${src_lan}
	decode_to_file=${output}/${test_file##*/}.${tgt_lan}.${prefix}.tgt.${now_time}
	log_file=${output}/${prefix}.log.${now_time}

	cmd="python ../tensor2tensor/bin/t2t_decoder.py --t2t_usr_dir=./work_dir --output_dir=./model --data_dir=$data_dir --problems=$problems --decode_hparams=beam_size=5,alpha=0.6 --model=transformer --hparams_set=$hparams --checkpoint_path=${ckpt_path} --decode_from_file=$decode_from_file --decode_to_file=$decode_to_file"
	echo ${cmd}
	${cmd}

	sed -i "s/@@ //g" $decode_to_file
	sh calc_metrics.sh $test_file $decode_to_file ${src_lan} ${tgt_lan} >> $log_file
	echo $st,' eval successful!'
	st=$[$st+5000]

done
