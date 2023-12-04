export const normalizeObj = arr => {
    const obj = {};
    arr.forEach(el => obj[el.id] = el);
    return obj;
}

export const DAYS = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

export const CATEGORIES = [
  "Amphibians",
  "Arthropods",
  "Birds",
  "Cats",
  "Dogs",
  "Marines",
  "Other Mammals",
  "Other Critters",
  "Rabbits",
  "Reptiles",
  "Rodents",
]


export const formatBusinessHours = (obj) => {
    const errors = []
    const businessHours = DAYS.map(day => {
      const {active, open, close} = obj[day]
      const hours = active ? open+"-"+close : "Closed"

      if (active && (!open || !close)) {
        errors.push(`Please set your shop's hours on ${day}.`)
      }

      else if (active && open >= close) {
        errors.push(`Opening hours must be before closing hours on ${day}.`)
      }

      return `${day} ${hours}`
    }).join("\n")

    if (errors.length) throw Error(errors.join("\n"))

    console.log("🚀 ~ file: utils.js:44 ~ formatBusinessHours ~ businessHours:", businessHours)
    return businessHours
}

export const formatPhoneNumber = (num) => {
    return `(${num.slice(0,3)}) ${num.slice(3,6)}-${num.slice(6)}`
}

export const parseBusinessHours = (str) => {
    if (!str) return null

    const hoursObj = {}

    // ["Mon 00:00-00:00", ...]
    str.split(/\r?\n/).forEach(ele => {
        let [day, time] = ele.split(" ")
        if (time.endsWith("/r")) time = time.splice(-2,2)
        const [open, close, active] =
            time==="Closed" ?
                ["","",false]
                : [...time.split("-"), true]

        hoursObj[day] = {open, close, active}
    })

    return hoursObj;
}
