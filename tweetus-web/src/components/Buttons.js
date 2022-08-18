import React,{useState} from 'react'

function Button({action,style,tweet}) {
    const className = style ? style : 'btn btn-dark'
    const  [like,setLike] =useState(tweet.likes ? tweet.likes : 0)
    const [onsecondtimeclick,setOnsecondtimeclick]= useState(false)
    const actionsdisplay = action.display ? action.display : 'Action'
    const display =action.type === "Likes" ? `${like} ${actionsdisplay}` : `${actionsdisplay}`
    const handleonClick =(ev) =>{
      ev.preventDefault()
      if(action.type ==='Likes'){
        if(onsecondtimeclick === true){
          setLike(like -1)
          setOnsecondtimeclick(false)
        }else
        {
          setLike(tweet.likes +1)// here using useState we are changing updating the likes
          setOnsecondtimeclick(true)
        }
        

        // like=tweet.likes +1 // this line will not save the values because in function we need to use
        //hooks (useState) to save the changes(and also to display)   
      }
    }
    return (
   <button  className={className} onClick={handleonClick}>{display}</button>
    )
}

export default Button