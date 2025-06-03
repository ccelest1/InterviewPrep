/**
 Worked on algo for submitting random exam when pressing on random exam button -> use random submitted and add/delete as necessary
 ended up going with a simpler approach that rectified any null/undefined errors
 */

const randomExam = (dummy) => {
    let RE = {
        "adminId": Math.floor(Math.random() * dummy.length)
    }
    const origin = dummy[0]
    Object.keys(origin).map((key) => {
        if (!RE[key] && key !== "__v" && key !== "_id") {
            const object = dummy[Math.floor(Math.random() * dummy.length - 1)]
            if (object) {
                if (key == 'examId') {
                    RE['examTypeId'] = object['examId']
                } else {
                    if (object[key] !== "" || object[key] !== null) {
                        RE[key] = object[key]
                    }
                    if (!object[key]) {
                        RE[key] = Math.floor(Math.random() * dummy.length)
                    }
                }
            }
        }
        if (Object.keys(RE) !== Object.keys(origin)) {
            RE = origin
            delete RE['__v']
            delete RE['_id']
        }
    })
    handleSubmit(RE)
}
