#!/bin/bash

# This script runs rdf-doctor with the data files in the specified directory as input.
# For example
# bash exec_rdf-doctor_with_data.sh test_files output

if [ $# -ne 2 ]; then
  echo "$# arguments were specified." 1>&2
  echo "Requires two argument to run." 1>&2
  echo "The first argument specifies the directory containing the input files." 1>&2
  echo "The second argument specifies the directory to output the results." 1>&2
  exit 1
fi

CURRENT_DIR=`dirname $0`
INPUT_FILE_DIR=$1
DATE=`date '+%Y%m%d_%H%M%S'`
DATASET_NAME=`basename ${INPUT_FILE_DIR}`
OUTPUT_DIR=$2
LOG_DIR=${OUTPUT_DIR}/log
LOG_OUT=${LOG_DIR}/${DATASET_NAME}_stdout_${DATE}.log
LOG_ERR=${LOG_DIR}/${DATASET_NAME}_stderr_${DATE}.log

if [ ! -d ${INPUT_FILE_DIR} ]; then
  echo "The specified arguments are invalid. No test data exists." 1>&2
  exit 1
fi

if [ ! -d ${OUTPUT_DIR} ]; then
  mkdir -p ${OUTPUT_DIR}
fi

if [ ! -d ${LOG_DIR} ]; then
  mkdir -p ${LOG_DIR}
fi

exec 1> >(tee -a $LOG_OUT)
exec 2>>$LOG_ERR

FILES=`find ${INPUT_FILE_DIR} -name '*.ttl' -or -name '*.nt' -or -name '*.ttl.gz' -or -name '*.nt.gz'`

for F in ${FILES}; do
  if [ -f ${F} ] ; then
    INPUT_FILES_PATH+=("${F}")
  fi
done

function print_file_info() {
  INPUT_FILE_NAME=`basename ${INPUT_FILE_PATH}`
  FILE_SIZE=`wc -c < ${INPUT_FILE_PATH}`
  if [ ${FILE_SIZE} -lt 1024 ]; then
    FILE_SIZE="$(printf %.2f $(echo "scale=2; ${FILE_SIZE}" | bc)) B"
  elif [ ${FILE_SIZE} -lt 1048576 ]; then
    FILE_SIZE="$(printf %.2f $(echo "scale=2; ${FILE_SIZE}/1024" | bc)) KB"
  elif [ ${FILE_SIZE} -lt 1073741824 ]; then
    FILE_SIZE="$(printf %.2f $(echo "scale=2; ${FILE_SIZE}/1048576" | bc)) MB"
  else
    FILE_SIZE="$(printf %.2f $(echo "scale=2; ${FILE_SIZE}/1073741824" | bc)) GB"
  fi

  echo "${INPUT_FILE_NAME} (${FILE_SIZE})"
}

function print_run_time() {
  SS=`expr ${END_TIME} - ${START_TIME}`

  HH=`expr ${SS} / 3600`
  SS=`expr ${SS} % 3600`
  MM=`expr ${SS} / 60`
  SS=`expr ${SS} % 60`

  echo "$(printf "%02dh %02dm %02ds" ${HH} ${MM} ${SS})"
}

function exec_doctor() {
  print_file_info

  START_TIME=`date +%s`
  rdf-doctor -i ${INPUT_FILE_PATH} -re -o ${OUTPUT_DIR}
  END_TIME=`date +%s`
  print_run_time
}

for INPUT_FILE_PATH in "${INPUT_FILES_PATH[@]}"
do
  exec_doctor
  echo ''
done
