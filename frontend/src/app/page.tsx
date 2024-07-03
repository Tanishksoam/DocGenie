import Link from "next/link";

const HomePage = () => (
  <div>
    <h1 className="text-2xl font-bold">Welcome to DocuManageAI</h1>
    <Link href="/upload">
      <p className="text-blue-500">Upload Document</p>
    </Link>
  </div>
);

export default HomePage;
