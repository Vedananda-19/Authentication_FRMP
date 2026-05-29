import { useNavigate } from "react-router-dom"

function HomePage(){
    const navigate = useNavigate()
    return( 
        <div>
            <button onClick={() => navigate("/login")}>Login</button>
            <button onClick={() => navigate("/register")}>Register</button>
            <button>Admin</button>
        </div>
    )
}

export default HomePage