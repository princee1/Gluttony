
function buldBot() {
    echo "Building..."
    pyinstaller --hidden-import pyexcel_io.readers.csv_in_file --hidden-import pyexcel_io.readers.csv_in_memory --hidden-import pyexcel_io.readers.csv_content --hidden-import pyexcel_io.readers.csvz --hidden-import pyexcel_io.writers.csv_in_file --hidden-import pyexcel_io.writers.csv_in_memory --hidden-import pyexcel_io.writers.csvz_writer --hidden-import pyexcel_io.database.importers.django --hidden-import pyexcel_io.database.importers.sqlalchemy --hidden-import pyexcel_io.database.exporters.django  --hidden-import pyexcel_io.database.exporters.sqlalchemy --clean --distpath /bot --workpath /bin  --add-data "c:/users/david/appdata/local/packages/pythonsoftwarefoundation.python.3.9_qbz5n2kfra8p0/localcache/local-packages/python39/site-packages/pyfiglet;./pyfiglet"  bot/lib/main/Gluttony.py

}

function createModule() {
    mkdir "$1"
    REQUEST="${1}/${1}_request"
    COMMON="${1}/common"
    QUESTIONUI="${1}/question_ui"

    touch "mainExecitionManager.py"

    mkdir "${REQUEST}" "${COMMON}" "${QUESTIONUI}"
    touch "${COMMON}/_account.py" "${COMMON}/_csvData.py" "${COMMON}/_raffle.py"
    touch "${QUESTIONUI}/${1}_question.py"

}

function clean() {
    echo "Cleaning..."
    sleep 2
}

function intro(){
    echo "**** Glutonny ****"
    pwd  -P
    echo ""
}

function main() {
    intro
    while read -p ">>" CMD
        do
            case $CMD in "clean") 
                clean 
                clear ;;
            "build") 
                build 
                clear ;;
            "exit")
                exit 0 ;;
            *) 
                echo "Try again: $CMD did not match any command";;
            esac  
        done
}

main