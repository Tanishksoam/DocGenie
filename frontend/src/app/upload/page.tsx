"use client";

import { useState } from "react";
import UploadForm from "components/UploadForm";

const UploadPage = () => {
  const [result, setResult] = useState<any>(null);

  const handleUpload = async (formData: FormData) => {
    const response = await fetch("/api/upload", {
      method: "POST",
      body: formData,
    });
    const data = await response.json();
    setResult(data);
  };

  return (
    <div>
      <h1 className="text-2xl font-bold">Upload Document</h1>
      <UploadForm onUpload={handleUpload} />
      {result && (
        <div>
          <h2 className="text-xl font-semibold">Text Content</h2>
          <p>{result.text}</p>
          <h2 className="text-xl font-semibold">Analysis</h2>
          <p>Sentiment: {result.analysis.sentiment}</p>
          <p>
            Confidence Scores:{" "}
            {JSON.stringify(result.analysis.confidence_scores)}
          </p>
        </div>
      )}
    </div>
  );
};

export default UploadPage;
