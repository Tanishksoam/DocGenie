import "../styles/globals.css";
import { ReactNode } from "react";

const Layout = ({ children }: { children: ReactNode }) => (
  <html lang="en">
    <body className="container mx-auto p-4">{children}</body>
  </html>
);

export default Layout;
