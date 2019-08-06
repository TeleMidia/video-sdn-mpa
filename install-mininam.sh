#!/bin/bash

wget http://www.cs.ucc.ie/~ak18/MiniNAM/code/MiniNAM.tar.gz
tar -xzf MiniNAM.tar.gz
mv MiniNAM/MiniNAM MiniNAM-bin
mv paping/paping .
chmod +x MiniNAM
chmod +x paping