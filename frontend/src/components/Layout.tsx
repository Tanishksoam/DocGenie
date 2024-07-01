import { ReactNode } from "react";
import Head from "next/head";

interface LayoutProps {
  children: ReactNode;
  title?: string;
}

const Layout = ({ children, title = "DocuManageAI" }: LayoutProps) => {
  return (
    <div>
      <Head>
        <title>{title}</title>
        <meta name="description" content="Document management using AI" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <header className="bg-blue-500 text-white p-4">
        <h1 className="text-2xl">DocuManageAI</h1>
      </header>
      <main className="container mx-auto p-4">{children}</main>
      <footer className="bg-gray-800 text-white p-4 text-center">
        <p>&copy; 2024 DocuManageAI. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default Layout;
