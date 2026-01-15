import Sidebar from "./Sidebar";
import Topbar from "./Topbar";

type props ={
    children: React.ReactNode;
}

function AppLayout({children}:props){
    return(
        <div>
            <Topbar />
            <div style={{ display: "flex" }}>
                <Sidebar />
                <main style={{ flexGrow: 1, padding: "1rem" }}>{children}</main>
            </div>

        </div>
    );
}

export default AppLayout;

