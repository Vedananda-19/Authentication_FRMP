import {useState} from "react"
import {useNavigate} from "react-router-dom"

function RegisterPage(){
    const handleRegister = (e:React.SubmitEvent) => {
        return null
    }
    return(
        <div className="backgroundDiv">
            <div className="centerCard">
                <form className="authForm" onSubmit={handleRegister}>
                    <input type="text" placeholder="username" />
                    <input type="password" placeholder="password" />
                    <input type="password" placeholder="confirm password" />
                    <input type="date" placeholder="date of birth" />
                    <button type="submit">Register</button>
                </form> 
            </div>
        </div>
    )
}

export default RegisterPage