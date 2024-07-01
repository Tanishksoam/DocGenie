const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:5000";

export const uploadDocument = async (formData: FormData) => {
  try {
    const response = await fetch(`${API_URL}/upload`, {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error uploading document:", error);
    throw error;
  }
};
