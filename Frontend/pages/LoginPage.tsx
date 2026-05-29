import { useState } from "react";

function LoginPage() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [errorMsg, setErrorMsg] = useState("");
    async function handleLogin(e: React.SubmitEvent) {
        e.preventDefault();
        console.log("Form Entered");
        const formData = { username: username, password: password };
        try {
            const response = await fetch("/api/login", {
                method: "POST",
                headers: { "Content-type": "application.json" },
                body: JSON.stringify(formData),
            });
            const data = await response.json();
            console.log(data);
            console.log(response);
            if (data == "successful") console.log("successful");
            else setErrorMsg("Invalid Credentials");
        } catch (error) {
            console.log(error);
            setErrorMsg("An Error Occured");
        }
    }
    return (
        <div className="backgroundDiv">
            <div className="centerCard">
                <form className="authForm" onSubmit={handleLogin}>
                    <input
                        type="text"
                        placeholder="username"
                        onChange={(e) => setUsername(e.target.value)}
                        value={username}
                        required
                    />
                    <input
                        type="password"
                        placeholder="password"
                        onChange={(e) => setPassword(e.target.value)}
                        value={password}
                        required
                    />
                    <button type="submit">Login</button>
                    {errorMsg && <p>{errorMsg}</p>}
                </form>
            </div>
        </div>
    );
}

export default LoginPage;
