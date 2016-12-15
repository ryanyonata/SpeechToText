#!/bin/bash

if [ $1 = "file" ]; then
	#statements
	julius -input file -C julius/asr.jconf -plugindir julius/plugin/linux
else
	julius -input mic -C julius/asr.jconf -plugindir julius/plugin/linux
fi